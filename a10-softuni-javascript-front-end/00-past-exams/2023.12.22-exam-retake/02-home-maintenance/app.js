window.addEventListener("load", solve);

function solve() {
  const placeInput = document.getElementById("place");
  const actionInput = document.getElementById("action");
  const personInput = document.getElementById("person");
  const addBtn = document.getElementById("add-btn");
  const taskList = document.getElementById("task-list");
  const doneList = document.getElementById("done-list");

  addBtn.addEventListener("click", () => {
    const place = placeInput.value.trim();
    const action = actionInput.value.trim();
    const person = personInput.value.trim();

    if (!place || !action || !person) {
      return;
    }

    // Create new list item for task-list
    const listItem = document.createElement("li");
    listItem.classList.add("clean-task");

    const article = document.createElement("article");
    const placeParagraph = document.createElement("p");
    placeParagraph.textContent = `Place:${place}`;
    const actionParagraph = document.createElement("p");
    actionParagraph.textContent = `Action:${action}`;
    const personParagraph = document.createElement("p");
    personParagraph.textContent = `Person:${person}`;

    article.appendChild(placeParagraph);
    article.appendChild(actionParagraph);
    article.appendChild(personParagraph);
    listItem.appendChild(article);

    const buttonsDiv = document.createElement("div");
    buttonsDiv.classList.add("button");

    const editBtn = document.createElement("button");
    editBtn.classList.add("edit");
    editBtn.textContent = "Edit";
    buttonsDiv.appendChild(editBtn);

    const doneBtn = document.createElement("button");
    doneBtn.classList.add("done");
    doneBtn.textContent = "Done";
    buttonsDiv.appendChild(doneBtn);

    listItem.appendChild(buttonsDiv);
    taskList.appendChild(listItem);

    // Clear input fields
    placeInput.value = "";
    actionInput.value = "";
    personInput.value = "";

    // Edit button functionality
    editBtn.addEventListener("click", () => {
      placeInput.value = place;
      actionInput.value = action;
      personInput.value = person;
      taskList.removeChild(listItem);
    });

    // Done button functionality
    doneBtn.addEventListener("click", () => {
      taskList.removeChild(listItem);
      buttonsDiv.removeChild(editBtn);
      buttonsDiv.removeChild(doneBtn);

      const deleteBtn = document.createElement("button");
      deleteBtn.classList.add("delete");
      deleteBtn.textContent = "Delete";
      listItem.appendChild(deleteBtn);

      doneList.appendChild(listItem);

      // Delete button functionality
      deleteBtn.addEventListener("click", () => {
        doneList.removeChild(listItem);
      });
    });
  });
}

solve();
