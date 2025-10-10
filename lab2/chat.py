import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from util import chat_ollama

def run_conversation():
    """Demonstrate multi-turn conversation."""
    
    messages = [
        {
            'role': 'system',
            'content': 'You are a helpful Python programming tutor.'
        },
        {
            'role': 'user',
            'content': 'What is a list comprehension?'
        }
    ]
    
    # Print First User Prompt
    print()
    print(messages[-1]["content"])

    # First response
    response = chat_ollama(messages, temperature=0.3)
    print("Assistant:", response)
    
    # Add to conversation
    messages.append({
        'role': 'assistant',
        'content': response
    })
    
    messages.append({
        'role': 'user',
        'content': 'Can you show me an example?'
    })
    
    # Print Second User Prompt
    print()
    print(messages[-1]["content"])

    # Second response
    response = chat_ollama(messages, temperature=0.3)
    print("\nAssistant:", response)


    # Add to conversation
    messages.append({
        'role': 'assistant',
        'content': response
    })
    
    messages.append({
        'role': 'user',
        'content': 'What are some limitations for python lists?'
    })
    
    # Print Third User Prompt
    print()
    print(messages[-1]["content"])

    # Third response
    response = chat_ollama(messages, temperature=0.3)
    print("\nAssistant:", response)

    # Add to conversation
    messages.append({
        'role': 'assistant',
        'content': response
    })
    
    messages.append({
        'role': 'user',
        'content': 'What are the pros and cons of a list comprehension instead of using a for loop to create a list?'
    })
    
    # Print Fourth User Prompt
    print()
    print(messages[-1]["content"])

    # Fourth response
    response = chat_ollama(messages, temperature=0.3)
    print("\nAssistant:", response)

if __name__ == "__main__":
    run_conversation()