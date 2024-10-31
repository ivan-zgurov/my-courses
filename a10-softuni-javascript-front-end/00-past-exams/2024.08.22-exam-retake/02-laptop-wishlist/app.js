window.addEventListener("load", solve);

function solve() {
  const addBtn = document.getElementById("add-btn");
  const laptopModelInput = document.getElementById("laptop-model");
  const storageInput = document.getElementById("storage");
  const priceInput = document.getElementById("price");
  const checkList = document.getElementById("check-list");
  const laptopsList = document.getElementById("laptops-list");
  const clearBtn = document.querySelector(".btn.clear");

  addBtn.addEventListener("click", () => {
    const model = laptopModelInput.value.trim();
    const storage = storageInput.value.trim();
    const price = priceInput.value.trim();

    if (!model || !storage || !price) {
      return;
    }

    const listItem = document.createElement("li");
    listItem.classList.add("laptop-item");

    const article = document.createElement("article");
    const modelParagraph = document.createElement("p");
    modelParagraph.textContent = model;
    const storageParagraph = document.createElement("p");
    storageParagraph.textContent = `Memory: ${storage} TB`;
    const priceParagraph = document.createElement("p");
    priceParagraph.textContent = `Price: ${price}$`;

    article.appendChild(modelParagraph);
    article.appendChild(storageParagraph);
    article.appendChild(priceParagraph);
    listItem.appendChild(article);

    const editBtn = document.createElement("button");
    editBtn.classList.add("btn", "edit");
    editBtn.textContent = "edit";

    const okBtn = document.createElement("button");
    okBtn.classList.add("btn", "ok");
    okBtn.textContent = "ok";

    listItem.appendChild(editBtn);
    listItem.appendChild(okBtn);
    checkList.appendChild(listItem);

    laptopModelInput.value = "";
    storageInput.value = "";
    priceInput.value = "";
    addBtn.disabled = true;

    editBtn.addEventListener("click", () => {
      laptopModelInput.value = model;
      storageInput.value = storage;
      priceInput.value = price;
      addBtn.disabled = false;
      checkList.removeChild(listItem);
    });

    okBtn.addEventListener("click", () => {
      checkList.removeChild(listItem);
      listItem.removeChild(editBtn);
      listItem.removeChild(okBtn);
      laptopsList.appendChild(listItem);
      addBtn.disabled = false;
    });
  });

  [laptopModelInput, storageInput, priceInput].forEach((input) => {
    input.addEventListener("input", () => {
      addBtn.disabled =
        !laptopModelInput.value.trim() ||
        !storageInput.value.trim() ||
        !priceInput.value.trim();
    });
  });

  clearBtn.addEventListener("click", () => {
    location.reload();
  });
}
