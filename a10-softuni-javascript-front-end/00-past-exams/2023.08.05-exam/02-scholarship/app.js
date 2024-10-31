window.addEventListener("load", solve);

function solve() {
  const studentInput = document.getElementById("student");
  const universityInput = document.getElementById("university");
  const scoreInput = document.getElementById("score");
  const nextBtn = document.getElementById("next-btn");
  const previewList = document.getElementById("preview-list");
  const candidatesList = document.getElementById("candidates-list");

  nextBtn.addEventListener("click", () => {
    const student = studentInput.value.trim();
    const university = universityInput.value.trim();
    const score = scoreInput.value.trim();

    if (!student || !university || !score) {
      return;
    }

    // Create new list item for preview-list
    const listItem = document.createElement("li");
    listItem.classList.add("application");

    const article = document.createElement("article");
    const studentHeading = document.createElement("h4");
    studentHeading.textContent = student;
    const universityParagraph = document.createElement("p");
    universityParagraph.textContent = `University: ${university}`;
    const scoreParagraph = document.createElement("p");
    scoreParagraph.textContent = `Score: ${score}`;

    article.appendChild(studentHeading);
    article.appendChild(universityParagraph);
    article.appendChild(scoreParagraph);
    listItem.appendChild(article);

    const editBtn = document.createElement("button");
    editBtn.classList.add("action-btn", "edit");
    editBtn.textContent = "edit";

    const applyBtn = document.createElement("button");
    applyBtn.classList.add("action-btn", "apply");
    applyBtn.textContent = "apply";

    listItem.appendChild(editBtn);
    listItem.appendChild(applyBtn);
    previewList.appendChild(listItem);

    // Clear input fields and disable Next button
    studentInput.value = "";
    universityInput.value = "";
    scoreInput.value = "";
    nextBtn.disabled = true;

    // Edit button functionality
    editBtn.addEventListener("click", () => {
      studentInput.value = student;
      universityInput.value = university;
      scoreInput.value = score;
      nextBtn.disabled = false;
      previewList.removeChild(listItem);
    });

    // Apply button functionality
    applyBtn.addEventListener("click", () => {
      previewList.removeChild(listItem);
      listItem.removeChild(editBtn);
      listItem.removeChild(applyBtn);

      candidatesList.appendChild(listItem);
      nextBtn.disabled = false;
    });
  });

  // Enable Next button when input fields are changed
  [studentInput, universityInput, scoreInput].forEach((input) => {
    input.addEventListener("input", () => {
      nextBtn.disabled =
        !studentInput.value.trim() ||
        !universityInput.value.trim() ||
        !scoreInput.value.trim();
    });
  });
}

solve();
