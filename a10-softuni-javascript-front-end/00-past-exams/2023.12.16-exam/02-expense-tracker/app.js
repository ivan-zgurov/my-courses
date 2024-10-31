// 90 / 100
window.addEventListener("load", solve);

function solve() {
  const expenseInput = document.getElementById("expense");
  const amountInput = document.getElementById("amount");
  const dateInput = document.getElementById("date");
  const addBtn = document.getElementById("add-btn");
  const previewList = document.getElementById("preview-list");
  const expensesList = document.getElementById("expenses-list");

  addBtn.addEventListener("click", () => {
    const expense = expenseInput.value.trim();
    const amount = amountInput.value.trim();
    const date = dateInput.value.trim();

    if (!expense || !amount || !date) {
      return;
    }

    // Create new list item for preview-list
    const listItem = document.createElement("li");
    listItem.classList.add("expense-item");

    const article = document.createElement("article");
    const expenseParagraph = document.createElement("p");
    expenseParagraph.textContent = `Type: ${expense}`;
    const amountParagraph = document.createElement("p");
    amountParagraph.textContent = `Amount: ${amount}$`;
    const dateParagraph = document.createElement("p");
    dateParagraph.textContent = `Date: ${date}`;

    article.appendChild(expenseParagraph);
    article.appendChild(amountParagraph);
    article.appendChild(dateParagraph);
    listItem.appendChild(article);

    const buttonsDiv = document.createElement("div");
    buttonsDiv.classList.add("buttons");

    const editBtn = document.createElement("button");
    editBtn.classList.add("btn", "edit");
    editBtn.textContent = "edit";
    buttonsDiv.appendChild(editBtn);

    const okBtn = document.createElement("button");
    okBtn.classList.add("btn", "ok");
    okBtn.textContent = "ok";
    buttonsDiv.appendChild(okBtn);

    listItem.appendChild(buttonsDiv);
    previewList.appendChild(listItem);

    // Clear input fields and disable Add button
    expenseInput.value = "";
    amountInput.value = "";
    dateInput.value = "";
    addBtn.disabled = true;

    // Edit button functionality
    editBtn.addEventListener("click", () => {
      expenseInput.value = expense;
      amountInput.value = amount;
      dateInput.value = date;
      addBtn.disabled = false;
      previewList.removeChild(listItem);
    });

    // Ok button functionality
    okBtn.addEventListener("click", () => {
      previewList.removeChild(listItem);
      buttonsDiv.removeChild(editBtn);
      buttonsDiv.removeChild(okBtn);

      const deleteBtn = document.createElement("button");
      deleteBtn.classList.add("btn", "delete");
      deleteBtn.textContent = "Delete";
      listItem.appendChild(deleteBtn);

      expensesList.appendChild(listItem);
      addBtn.disabled = false;

      // Delete button functionality
      deleteBtn.addEventListener("click", () => {
        location.reload();
      });
    });
  });

  // Enable Add button when input fields are changed
  [expenseInput, amountInput, dateInput].forEach((input) => {
    input.addEventListener("input", () => {
      addBtn.disabled =
        !expenseInput.value.trim() ||
        !amountInput.value.trim() ||
        !dateInput.value.trim();
    });
  });
}

solve();
