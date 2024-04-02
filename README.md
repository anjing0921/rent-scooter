# C21 Applicant Technical Assessment

## Introduction

This assessment will be used to evaluate your technical skills and problem-solving abilities. It will also provide insight into your coding style, approach to software development, and overall understanding of programming concepts. Please read through the following instructions carefully.

The assessment consists of *two parts*: a coding challenge where you will be asked to implement several routes for a REST API, and a UI/UX challenge where you will be asked to describe the React components needed to implement the frontend of the web application. You are required to complete both parts of the assessment.

After completing the assessment, you will be asked to schedule a follow-up interview to discuss your solution and answer any questions about your implementation.

## Part One: Scooter Rental API Implementation

The first part of the assessment is to implement three routes for a REST API that will be used to manage a scooter rental service. For this part of the assessment, please refer to the following ERD to understand the data model and relationships between the entities: [Scooter Rental ERD](schema_diagram/scooter_rental_schema.png)

Feel free to use whichever programming language, framework, or libraries you are most comfortable with.

For this assessment, you will be implementing the following routes:
- Retrieve a list of all scooters, with a filter query for limiting the list based on availability
- Rent an available scooter
    - A customer should only be able to rent a scooter if it is not already currently being rented by another customer.
    - A customer should only be able to rent a scooter if they are not currently renting another scooter.
    - A customer should only be able to rent a scooter if it is >15% charged.
- Return a rented scooter
    - The rental history should remain intact - rental history should not be deleted when a scooter is returned.
    - Once a scooter is returned, it is available to rent by another customer. 

It is up to you to decide which RESTful verbs to use for each route, and how to structure the request and response bodies.

As always, it is important to ensure the code you write is working on your local machine, as expected. It is not a requirement to deploy your solution to a hosting service, though you are free to do so.

You may refer to the CSV files and the SQL file provided for example data and to set up your database. It is not a requirement to utilize these files, they are provided for your convenience. If you are finding it difficult to integrate these files into your solution, feel free to ignore or remove them. 

*Note*: You may see a failing build in the GitHub Actions tab. Feel free to ignore these build failures, as they are not related to the assessment and will not affect your submission.

## Part Two: UI/UX Challenge

The second part of the assessment is to describe the React components needed to implement the frontend of the web application. For this part of the assessment, please refer to the following wireframes to understand the layout and user interface of the web application: https://www.figma.com/file/OhepVfumZceO3DRdt1zlYh/Ada's-Scooter-Rental?type=design&node-id=0-1&mode=design. 

Please provide your solution to this part of the assessment using a diagram. Feel free to use any software or application (such as Google Drawings) to create your diagram.

Please note it is *not* a requirement for you to code an implementation of the frontend. You are only required to describe the React components needed to implement the frontend.

For this part of the assessment, please describe the following:
- Name of the React component, and its use case
- The prop(s) the component will need to function
- The flow of data between components

## Assessment Submission

You can start working on your solution by cloning this repo, making changes in your local environment and pushing commits to this repository. After you have completed the assessment, please refer to the email you received from CodeScreen to access the Assessment Screen and submit your solution.
## License

At CodeScreen, we strongly value the integrity and privacy of our assessments. As a result, this repository is under exclusive copyright, which means you **do not** have permission to share your solution to this test publicly (i.e., inside a public GitHub/GitLab repo, on Reddit, etc.). <br>

## Submitting your solution

Please push your changes to the `main branch` of this repository. You can push one or more commits. <br>

Once you are finished with the task, please click the `Submit Solution` link on <a href="https://app.codescreen.com/candidate/36d90bf0-6cc9-484c-8eed-7a8c8592940c" target="_blank">this screen</a>.