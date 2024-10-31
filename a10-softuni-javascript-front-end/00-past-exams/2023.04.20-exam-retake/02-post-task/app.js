window.addEventListener("load", solve);

function solve() {
  const titleInput = document.getElementById("task-title");
  const categoryInput = document.getElementById("task-category");
  const contentInput = document.getElementById("task-content");
  const publishBtn = document.getElementById("publish-btn");
  const reviewList = document.getElementById("review-list");
  const publishedList = document.getElementById("published-list");

  publishBtn.addEventListener("click", () => {
    const title = titleInput.value.trim();
    const category = categoryInput.value.trim();
    const content = contentInput.value.trim();

    if (!title || !category || !content) {
      return;
    }

    // Create new list item for review-list
    const listItem = document.createElement("li");
    listItem.classList.add("rpost");

    const article = document.createElement("article");
    const titleHeading = document.createElement("h4");
    titleHeading.textContent = title;
    const categoryParagraph = document.createElement("p");
    categoryParagraph.textContent = `Category: ${category}`;
    const contentParagraph = document.createElement("p");
    contentParagraph.textContent = `Content: ${content}`;

    article.appendChild(titleHeading);
    article.appendChild(categoryParagraph);
    article.appendChild(contentParagraph);
    listItem.appendChild(article);

    const editBtn = document.createElement("button");
    editBtn.classList.add("action-btn", "edit");
    editBtn.textContent = "Edit";

    const postBtn = document.createElement("button");
    postBtn.classList.add("action-btn", "post");
    postBtn.textContent = "Post";

    listItem.appendChild(editBtn);
    listItem.appendChild(postBtn);
    reviewList.appendChild(listItem);

    // Clear input fields
    titleInput.value = "";
    categoryInput.value = "";
    contentInput.value = "";

    // Edit button functionality
    editBtn.addEventListener("click", () => {
      titleInput.value = title;
      categoryInput.value = category;
      contentInput.value = content;
      reviewList.removeChild(listItem);
    });

    // Post button functionality
    postBtn.addEventListener("click", () => {
      reviewList.removeChild(listItem);
      listItem.removeChild(editBtn);
      listItem.removeChild(postBtn);
      publishedList.appendChild(listItem);
    });
  });
}

solve();
