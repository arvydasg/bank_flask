# bank_flask

Padaryti programą, kurį leistų įvesti asmenis, bankus, asmenims
priskirti sąskaitas bankuose.

- Asmuo turi vardą, pavardę, asmens kodą, tel. numerį.
- Bankas turi pavadinimą, adresą, banko kodą, SWIFT kodą
- Sąskaita turi numerį, balansą, priskirtą asmenį ir banką
- Asmuo gali turėti daug sąskaitų tame pačiame arba skirtinguose
bankuose
- Padaryti duomenų bazės schemą (galima ją parodyti dėstytojui).
- Sukurti programą su UI konsolėje, kuri leistų įvesti asmenis,
  bankus, sąskaitas. Leistų vartotojui peržiūrėti savo sąskaitas ir jų
  informaciją, pridėti arba nuimti iš jų pinigų. Taip pat leistų
  bendrai peržiūrėti visus bankus, vartotojus, sąskaitas ir jų
  informaciją.

## Possible improvements

Chatgpt suggestions:

- Input validation: Currently, the program assumes that the user
  inputs are valid and does not handle any exceptions. Adding input
  validation will make the program more robust and user-friendly.

- User Interface: The current command-line interface can be improved
  by adding menus, submenus, and prompts to guide the user through the
  program. This will make it easier for users to navigate and use the
  program.

- Error handling: The program should handle errors gracefully and
  provide meaningful error messages to the user when things go wrong.
  This will help users understand what went wrong and how to correct
  it.

- Security: The program should handle sensitive data such as passwords
  securely. It should also protect against SQL injection attacks.

- Better naming conventions: Some of the variable names in the program
  are not descriptive enough, making it difficult to understand what
  they are used for. Using descriptive variable names will make the
  program easier to read and understand.

- Refactoring: The code can be refactored to make it more modular,
  reusable, and maintainable. For example, some of the code in the
  main.py file can be moved to separate functions or classes to
  improve readability and maintainability.

- Unit testing: Adding unit tests to the program will help ensure that
  it works as expected and prevent regressions when changes are made.
