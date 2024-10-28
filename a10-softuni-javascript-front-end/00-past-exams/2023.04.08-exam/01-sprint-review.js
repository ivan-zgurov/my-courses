function sprintReview(input) {
  const n = Number(input.shift());
  const board = {};

  for (let i = 0; i < n; i++) {
    const [assignee, taskId, title, status, estimatedPoints] = input
      .shift()
      .split(":");
    if (!board[assignee]) {
      board[assignee] = [];
    }
    board[assignee].push({
      taskId,
      title,
      status,
      estimatedPoints: Number(estimatedPoints),
    });
  }

  for (let commandLine of input) {
    if (commandLine === "End") {
      break;
    }

    const [command, ...args] = commandLine.split(":");

    switch (command) {
      case "Add New": {
        const [assignee, taskId, title, status, estimatedPoints] = args;
        if (!board[assignee]) {
          console.log(`Assignee ${assignee} does not exist on the board!`);
        } else {
          board[assignee].push({
            taskId,
            title,
            status,
            estimatedPoints: Number(estimatedPoints),
          });
        }
        break;
      }

      case "Change Status": {
        const [assignee, taskId, newStatus] = args;
        if (!board[assignee]) {
          console.log(`Assignee ${assignee} does not exist on the board!`);
        } else {
          const task = board[assignee].find((task) => task.taskId === taskId);
          if (!task) {
            console.log(
              `Task with ID ${taskId} does not exist for ${assignee}!`
            );
          } else {
            task.status = newStatus;
          }
        }
        break;
      }

      case "Remove Task": {
        const [assignee, index] = args;
        const taskIndex = Number(index);
        if (!board[assignee]) {
          console.log(`Assignee ${assignee} does not exist on the board!`);
        } else if (taskIndex < 0 || taskIndex >= board[assignee].length) {
          console.log(`Index is out of range!`);
        } else {
          board[assignee].splice(taskIndex, 1);
        }
        break;
      }

      default:
        break;
    }
  }

  const points = {
    ToDo: 0,
    "In Progress": 0,
    "Code Review": 0,
    Done: 0,
  };

  for (const tasks of Object.values(board)) {
    for (const task of tasks) {
      points[task.status] += task.estimatedPoints;
    }
  }

  console.log(`ToDo: ${points.ToDo}pts`);
  console.log(`In Progress: ${points["In Progress"]}pts`);
  console.log(`Code Review: ${points["Code Review"]}pts`);
  console.log(`Done Points: ${points.Done}pts`);

  const totalOtherPoints =
    points.ToDo + points["In Progress"] + points["Code Review"];
  if (points.Done >= totalOtherPoints) {
    console.log("Sprint was successful!");
  } else {
    console.log("Sprint was unsuccessful...");
  }
}

// Test Case #1:
sprintReview([
  "5",
  "Kiril:BOP-1209:Fix Minor Bug:ToDo:3",
  "Mariya:BOP-1210:Fix Major Bug:In Progress:3",
  "Peter:BOP-1211:POC:Code Review:5",
  "Georgi:BOP-1212:Investigation Task:Done:2",
  "Mariya:BOP-1213:New Account Page:In Progress:13",
  "Add New:Kiril:BOP-1217:Add Info Page:In Progress:5",
  "Change Status:Peter:BOP-1290:ToDo",
  "Remove Task:Mariya:1",
  "Remove Task:Joro:1",
]);

// Expected output:
// Task with ID BOP-1290 does not exist for Peter!
// Assignee Joro does not exist on the board!
// ToDo: 3pts
// In Progress: 8pts
// Code Review: 5pts
// Done Points: 2pts
// Sprint was unsuccessful...

// Test Case #2:
sprintReview([
  "4",
  "Kiril:BOP-1213:Fix Typo:Done:1",
  "Peter:BOP-1214:New Products Page:In Progress:2",
  "Mariya:BOP-1215:Setup Routing:ToDo:8",
  "Georgi:BOP-1216:Add Business Card:Code Review:3",
  "Add New:Sam:BOP-1237:Testing Home Page:Done:3",
  "Change Status:Georgi:BOP-1216:Done",
  "Change Status:Will:BOP-1212:In Progress",
  "Remove Task:Georgi:3",
  "Change Status:Mariya:BOP-1215:Done",
]);

// Expected output:
// Assignee Sam does not exist on the board!
// Assignee Will does not exist on the board!
// Index is out of range!
// ToDo: 0pts
// In Progress: 2pts
// Code Review: 0pts
// Done Points: 12pts
// Sprint was successful!
