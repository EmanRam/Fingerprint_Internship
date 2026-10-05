### Task 1:
#### what the `|` operator actually does.

- It is basically used to **connect different steps together in a pipeline**.

- From the task that I have done `chain = prompt | llm | StrOutputParser()`.
    - The prompt is first created and filled with the user’s input.
    - Then that prompt is sent to the LLM to generate a response.
    - Finally the  `StrOutputParser` takes the model’s response and converts it into a simple string. 
    - So instead of writing each step separately, `|` lets us chain them together in a clean and readable way.