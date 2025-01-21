# import paralleldots
# paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')

# def ner(text):
#     ner = paralleldots.ner(text)
#     return ner

# from transformers import pipeline
# import torch
# # Initialize the Hugging Face NER pipeline with GPU support (device=0 for GPU)
# device = 0 if torch.cuda.is_available() else -1  # Automatically choose GPU if available, otherwise fallback to CPU
# # Initialize the Hugging Face NER pipeline
# ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

# def ner(text):
#     # Use the Hugging Face pipeline to perform NER on the input text
#     ner = ner_pipeline(text)
#     return ner

# from transformers import pipeline
# import torch

# # Initialize the Hugging Face NER pipeline with GPU support
# device = 0 if torch.cuda.is_available() else -1  # Automatically choose GPU if available, otherwise fallback to CPU

# # Load the Hugging Face NER pipeline with a pre-trained model
# ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", device=device)

# def format_entities(entities):
#     # Initialize a dictionary to hold categorized entities
#     formatted_entities = {
#         'PERSON': [],
#         'LOCATION': [],
#         'ORGANIZATION': [],
#         'MISC': [],
#     }

#     # Merge sub-word tokens and categorize entities
#     for entity in entities:
#         word = entity['word'].replace("##", "")  # Merge sub-word tokens
#         entity_type = entity['entity']

#         if entity_type == 'I-PER':  # Person
#             formatted_entities['PERSON'].append(word)
#         elif entity_type == 'I-LOC':  # Location
#             formatted_entities['LOCATION'].append(word)
#         elif entity_type == 'I-ORG':  # Organization
#             formatted_entities['ORGANIZATION'].append(word)
#         else:  # Miscellaneous entities
#             formatted_entities['MISC'].append(word)

#     return formatted_entities

# def ner(text):
#     # Use the Hugging Face pipeline to perform NER on the input text
#     entities = ner_pipeline(text)
    
#     # Format the entities into a more readable structure
#     formatted_entities = format_entities(entities)
    
#     # Prepare the output to be more user-friendly
#     result = {
#         'text': text,
#         'entities': formatted_entities
#     }
    
#     return result

from transformers import pipeline
import torch

# Initialize the Hugging Face NER pipeline with GPU support
device = 0 if torch.cuda.is_available() else -1  # Automatically choose GPU if available, otherwise fallback to CPU

# Load the Hugging Face NER pipeline with a pre-trained model
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", device=device)

def map_entity_type(entity_type):
    """
    Maps the model's entity types to the desired output categories.
    """
    if entity_type == 'I-PER':
        return 'PERSON'
    elif entity_type == 'I-LOC':
        return 'LOCATION'
    elif entity_type == 'I-ORG':
        return 'ORGANIZATION'
    else:
        return 'MISC'

def format_entities(entities):
    formatted_entities = {
        'PERSON': [],
        'LOCATION': [],
        'ORGANIZATION': [],
        'MISC': [],
    }

    # Temporary variables to handle subword tokens
    current_entity = None
    current_entity_type = None
    current_entity_tokens = []
    current_entity_score = 0  # Store the score for the current entity

    for entity in entities:
        word = entity['word'].replace("##", "")  # Remove '##' from sub-token parts
        entity_type = entity['entity']
        score = float(entity['score'])  # Convert np.float32 to Python float

        # Map entity type from model's label to the desired label
        mapped_entity_type = map_entity_type(entity_type)

        if mapped_entity_type == current_entity_type:
            # Continue building the current entity and accumulate the score
            current_entity_tokens.append(word)
            # Use average of scores for entity if multiple tokens
            current_entity_score = (current_entity_score + score) / 2
        else:
            # If we were building a previous entity, add it to the formatted list
            if current_entity:
                formatted_entities[current_entity_type].append({
                    'name': "".join(current_entity_tokens),
                    'score': current_entity_score
                })

            # Start a new entity
            current_entity = word
            current_entity_type = mapped_entity_type
            current_entity_tokens = [word]
            current_entity_score = score  # Set the initial score for the new entity

    # Don't forget to add the last entity to the list
    if current_entity:
        formatted_entities[current_entity_type].append({
            'name': "".join(current_entity_tokens),
            'score': current_entity_score
        })

    # Remove categories that have no entities
    formatted_entities = {k: v for k, v in formatted_entities.items() if v}

    return formatted_entities

def ner(text):
    # Use the Hugging Face pipeline to perform NER on the input text
    entities = ner_pipeline(text)
    
    # Format the entities into a more readable structure
    formatted_entities = format_entities(entities)
    
    # Prepare the output to be more user-friendly
    result = {
        'text': text,
        'entities': formatted_entities
    }
    
    return result
