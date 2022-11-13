Created a system for uploading tasks with their completion status.

tasks() ==> Function will handle routes having POST,GET,DELETE functionalities.
User can add/delete single or multiple tasks at once.
User can get all the tasks at once.

singleTask() ==> User can also update/get/delete any single task by it's id.

errorMessage() ==> This function will return the error message

convertToJson() ==> This funciton will convert python dictionary to JSON 

makeTask() ==> This function will create a new task dictionary from user input

I have imported flask, request and Response for routing the backend.
uuid is imported for generating unique id, As uuid generates unique values using time stamp that's why it's very rare that collision happens.
I have also imported json for coverting python dictionary to json.
