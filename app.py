from flask import Flask, request, Response
import uuid
import json
app = Flask(__name__)

allTasks = {}


# IN THIS ROUTE WE HAVE IMPLEMENTED FOLLOWING FUNCTIONALITY
# POST A SINGLE TASK, RETURN ALL TASKS, POST MULTIPLE TASKS AT ONCE, DELETE MULTIPLE TASKS AT ONCE
@app.route("/v1/tasks/", methods=["GET", "POST", "DELETE"])
def tasks():
    if request.method == "POST":
        content = request.json
        result = {}
        result['tasks'] = []
        if 'tasks' in content:
            for tsk in content['tasks']:
                dic = makeTask(tsk)
                allTasks[dic['id']] = dic
                # allTasks.append(dic)
                result['tasks'].append({'id': dic['id']})
            final = convertToJson(result)
            return Response(final, status=201, mimetype='application/json')
        else:
            dic = makeTask(content)
            allTasks[dic['id']] = dic
            res = {'id': dic['id']}
            final = convertToJson(res)
            return Response(final, status=201, mimetype='application/json')
    elif request.method == "DELETE":
        content = request.json
        # print(content)

        for task in content['tasks']:
            key = task['id']
            if key in allTasks:
                del allTasks[key]

        return Response(status=204, mimetype='application/json')
    else:
        allCurrentTask = []
        for key in allTasks:
            allCurrentTask.append(allTasks[key])
        res = {'tasks': allCurrentTask}
        final = convertToJson(res)
        return Response(final, status=200, mimetype='application/json')


# IN THIS ROUTE WE HAVE IMPLEMENTED FOLLOWING FUNCTIONALITY
# GET SPECIFIC TASK, DELETE SPECIFIC TASK, UPDATE SPECIFIC TASK
@app.route("/v1/tasks/<int:getId>", methods=["GET", "PUT", "DELETE"])
def singleTask(getId):
    if request.method == "GET":
        if getId in allTasks:
            final = convertToJson(allTasks[getId])
            return Response(final, status=200, mimetype='application/json')
        return errorMessage()
    elif request.method == "DELETE":
        if getId in allTasks:
            del allTasks[getId]
        return Response(status=204, mimetype='application/json')
    elif request.method == "PUT":
        content = request.json
        if getId in allTasks:
            allTasks[getId]['title'] = content['title']
            allTasks[getId]['is_completed'] = content['is_completed']

            return Response(status=204, mimetype='application/json')
        return errorMessage()

# THIS FUNCTION IS USED FOR REFLECTING NOT FOUND ERROR


def errorMessage():
    error = {}
    error['error'] = 'There is no task at that id'
    final = convertToJson(error)
    return Response(final, status=404, mimetype='application/json')

# THIS FUNCTION IS USED FOR CONVERTING PYTHON DATA STRUCTURES TO JSON


def convertToJson(arg):
    final = json.dumps(arg, indent=4)
    return final

# THIS FUNCTION IS USED FOR CREATING A DICTIONARY FROM USER PASSED OBJECT


def makeTask(task):
    taskTitle = task['title']
    uniqueId = uuid.uuid1().int >> 64
    # uniqueId = 1
    dic = {"id": uniqueId, "title": taskTitle,
           "is_completed": False}
    # print(dic)
    return dic


app.run(debug=True)
