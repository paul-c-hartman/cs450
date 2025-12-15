from context import ConversationManager

conversation = ConversationManager(
    system_prompt="You are a software engineer with many years of experience. You value short, efficient communications, write code that works and is easy to maintain, and state your thoughts clearly.",
    max_history=6
)

prompt = "Based on popular implementations of the classic game Snake, what are 2 of the best customizations for this game? Do not provide any examples."
conversation.add_user_message(prompt)
print(f"Prompt: {prompt}")
response = conversation.get_response()
print(f"Response:\n{response}")

prompt = "Create a Python snake game which implements those features in Pygame in under 500 lines of code"
conversation.add_user_message(prompt)
print(f"Prompt: {prompt}")
response = conversation.get_response()
print(f"Response: {response}")