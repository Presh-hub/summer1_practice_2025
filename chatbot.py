import spacy

# Load the SpaCy model
try:
    nlp = spacy.load('en_core_web_sm')
    print("SpaCy model loaded successfully for preprocessing.")
except OSError:
    print("SpaCy model 'en_core_web_sm' not found. Please run 'python3 -m spacy download en_core_web_sm' in your activated virtual environment.")
    exit()

# Define your preprocessing function
def preprocess_text(text):
    """
    Processes text: tokenizes, lowercases, removes stop words and punctuation, and lemmatizes.
    """
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return tokens

# --- NEW/UPDATED CODE STARTS HERE ---

def generate_response(processed_query):
    """
    Generates a response based on the processed user query.
    Uses keyword matching for simple intent recognition.
    """
    # Join processed tokens back into a string for easier keyword searching
    # This allows checking for phrases or individual keywords efficiently
    query_str = " ".join(processed_query)

    # 1. Greetings and small talk
    if any(word in query_str for word in ["hello", "hi", "hey", "hola"]):
        return "Hello there! How can I assist you with your university-related questions today?"
    elif any(word in query_str for word in ["how are you", "how are things", "what's up", "you doing"]):
        return "As an AI, I don't have feelings, but I'm ready to help you! How can I assist you?"
    elif any(word in query_str for word in ["good morning", "good afternoon", "good evening"]):
        return "A pleasant time of day to you too! What's on your mind?"

    # 2. Questions about the bot itself
    elif any(word in query_str for word in ["who are you", "what are you", "your name"]):
        return "I am an AI-powered chatbot designed to assist students with their inquiries regarding university services, courses, and general information."
    elif any(word in query_str for word in ["what can you do", "help me", "your function", "abilities"]):
        return "I can answer common questions about university resources, course information, admissions, and guide you to the right departments. How can I help you specifically?"
    elif any(word in query_str for word in ["thank", "thanks", "appreciate"]):
        return "You're most welcome! I'm glad I could help."

    # 3. Specific help requests (can be expanded)
    elif "help" in query_str: # Catches "help me", "can you help" etc.
        return "Yes, I'm here to help! Please tell me what you need assistance with, for example, 'Where can I find information about financial aid?' or 'What are the requirements for course X?'"

    # 4. Farewell
    elif any(word in query_str for word in ["bye", "goodbye", "farewell", "see you"]):
        return "Goodbye! Feel free to return anytime if you have more questions."

    # Default response if no specific intent is recognized
    else:
        return "I'm designed to answer questions related to student support services. Could you please rephrase your question, or ask about a specific university topic?"

# Main chat loop
def chat():
    """
    Runs the main interactive chat session.
    """
    print("\n------------------------------------------------------")
    print("Welcome to the Student Support Chatbot!")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("------------------------------------------------------")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye! Have a great day.")
            break

        processed_input = preprocess_text(user_input)
        # print(f"DEBUG: Processed User Input: {processed_input}") # Uncomment for debugging

        response = generate_response(processed_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    
    # Start the interactive chat
    chat()