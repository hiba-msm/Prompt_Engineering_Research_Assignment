# English Prompt Variants


## Strategy: `simple`

### Variant 1

```text
Classify the following question into exactly one label: NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION. Answer with the label only.
```

### Variant 2

```text
Determine the correct class for the following question using one of these labels: NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION. Output only the label.
```

### Variant 3

```text
Read the question and assign exactly one class from: NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION. Return only the class name.
```

### Variant 4

```text
Your task is to classify the question into one of the following categories: NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION. Respond only with the category.
```

### Variant 5

```text
Identify the answer type of the question using exactly one of these labels: NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION. Do not explain.
```

### Variant 6

```text
Select the best label for the question from this set: NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION. Output the label only.
```

### Variant 7

```text
Choose one class for the question among NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION. Return only that class.
```

### Variant 8

```text
Assign a single category to the question from NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION. Answer with only the category name.
```


## Strategy: `definitions`

### Variant 1

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Now classify the following new question into exactly one label: NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION. Answer with the label only.
```

### Variant 2

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Using the definitions, examples, and disambiguation rule above when available, determine the correct answer type for the new question. Output only one label.
```

### Variant 3

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Read the new question carefully and assign the best matching label. Return only one label from the allowed set.
```

### Variant 4

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Your task is answer-type classification. Use the definitions, examples, and disambiguation rule above when available. Respond with exactly one category name only.
```

### Variant 5

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Identify what type of answer the new question is asking for. Choose only one of the six labels. Do not explain.
```

### Variant 6

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Classify the new question into the most appropriate answer type. Output the label only.
```

### Variant 7

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Select the single best class for the new question. The answer must be exactly one of: NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION.
```

### Variant 8

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Assign one category to the new question based on the expected answer type. Return only the category name.
```


## Strategy: `fewshot`

### Variant 1

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Now classify the following new question into exactly one label: NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION. Answer with the label only.
```

### Variant 2

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Using the definitions, examples, and disambiguation rule above when available, determine the correct answer type for the new question. Output only one label.
```

### Variant 3

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Read the new question carefully and assign the best matching label. Return only one label from the allowed set.
```

### Variant 4

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Your task is answer-type classification. Use the definitions, examples, and disambiguation rule above when available. Respond with exactly one category name only.
```

### Variant 5

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Identify what type of answer the new question is asking for. Choose only one of the six labels. Do not explain.
```

### Variant 6

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Classify the new question into the most appropriate answer type. Output the label only.
```

### Variant 7

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Select the single best class for the new question. The answer must be exactly one of: NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION.
```

### Variant 8

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Assign one category to the new question based on the expected answer type. Return only the category name.
```


## Strategy: `disambig`

### Variant 1

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Important DESCRIPTION vs ENTITY rule:
Choose DESCRIPTION when the question asks for an explanation, meaning, definition, function, purpose, use, or process.
Choose ENTITY when the question asks for the name of a specific object, animal, planet, language, currency, device, material, gas, software, element, metal, or instrument.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Now classify the following new question into exactly one label: NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION. Answer with the label only.
```

### Variant 2

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Important DESCRIPTION vs ENTITY rule:
Choose DESCRIPTION when the question asks for an explanation, meaning, definition, function, purpose, use, or process.
Choose ENTITY when the question asks for the name of a specific object, animal, planet, language, currency, device, material, gas, software, element, metal, or instrument.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Using the definitions, examples, and disambiguation rule above when available, determine the correct answer type for the new question. Output only one label.
```

### Variant 3

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Important DESCRIPTION vs ENTITY rule:
Choose DESCRIPTION when the question asks for an explanation, meaning, definition, function, purpose, use, or process.
Choose ENTITY when the question asks for the name of a specific object, animal, planet, language, currency, device, material, gas, software, element, metal, or instrument.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Read the new question carefully and assign the best matching label. Return only one label from the allowed set.
```

### Variant 4

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Important DESCRIPTION vs ENTITY rule:
Choose DESCRIPTION when the question asks for an explanation, meaning, definition, function, purpose, use, or process.
Choose ENTITY when the question asks for the name of a specific object, animal, planet, language, currency, device, material, gas, software, element, metal, or instrument.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Your task is answer-type classification. Use the definitions, examples, and disambiguation rule above when available. Respond with exactly one category name only.
```

### Variant 5

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Important DESCRIPTION vs ENTITY rule:
Choose DESCRIPTION when the question asks for an explanation, meaning, definition, function, purpose, use, or process.
Choose ENTITY when the question asks for the name of a specific object, animal, planet, language, currency, device, material, gas, software, element, metal, or instrument.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Identify what type of answer the new question is asking for. Choose only one of the six labels. Do not explain.
```

### Variant 6

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Important DESCRIPTION vs ENTITY rule:
Choose DESCRIPTION when the question asks for an explanation, meaning, definition, function, purpose, use, or process.
Choose ENTITY when the question asks for the name of a specific object, animal, planet, language, currency, device, material, gas, software, element, metal, or instrument.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Classify the new question into the most appropriate answer type. Output the label only.
```

### Variant 7

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Important DESCRIPTION vs ENTITY rule:
Choose DESCRIPTION when the question asks for an explanation, meaning, definition, function, purpose, use, or process.
Choose ENTITY when the question asks for the name of a specific object, animal, planet, language, currency, device, material, gas, software, element, metal, or instrument.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Select the single best class for the new question. The answer must be exactly one of: NUMBER, LOCATION, PERSON, DESCRIPTION, ENTITY, ABBREVIATION.
```

### Variant 8

```text
Use these label definitions:

NUMBER:
The expected answer is a number, date, year, quantity, measurement, percentage, or calculation result.

LOCATION:
The expected answer is a place, country, city, continent, region, river, mountain, desert, landmark, or geographical location.

PERSON:
The expected answer is a human person, fictional character, author, inventor, founder, president, artist, scientist, composer, or historical figure.

DESCRIPTION:
The expected answer requires an explanation, definition, meaning, purpose, function, process, use, or description.

ENTITY:
The expected answer is a concrete or named non-person, non-location, non-number item, such as an object, animal, planet, language, currency, software application, gas, element, metal, device, or instrument.

ABBREVIATION:
The question asks what an acronym, abbreviation, or shortened form stands for or means.

Important DESCRIPTION vs ENTITY rule:
Choose DESCRIPTION when the question asks for an explanation, meaning, definition, function, purpose, use, or process.
Choose ENTITY when the question asks for the name of a specific object, animal, planet, language, currency, device, material, gas, software, element, metal, or instrument.

Examples:
Question: How many colors are in a rainbow?
Label: NUMBER

Question: Where is the Statue of Liberty located?
Label: LOCATION

Question: Who wrote Pride and Prejudice?
Label: PERSON

Question: What is gravity?
Label: DESCRIPTION

Question: What is the function of the heart?
Label: DESCRIPTION

Question: What is a database used for?
Label: DESCRIPTION

Question: What tool is used to cut paper?
Label: ENTITY

Question: What planet is known as the Red Planet?
Label: ENTITY

Question: What does WHO stand for?
Label: ABBREVIATION

Assign one category to the new question based on the expected answer type. Return only the category name.
```
