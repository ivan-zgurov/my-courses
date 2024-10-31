// 80 / 100
window.addEventListener("load", solve);

function solve() {
  const typeInput = document.getElementById("type");
  const ageInput = document.getElementById("age");
  const genderInput = document.getElementById("gender");
  const adoptBtn = document.getElementById("adopt-btn");
  const adoptionInfo = document.getElementById("adoption-info");
  const adoptedList = document.getElementById("adopted-list");

  adoptBtn.addEventListener("click", (e) => {
    e.preventDefault();

    const type = typeInput.value.trim();
    const age = ageInput.value.trim();
    const gender = genderInput.value;

    if (!type || !age || !gender) {
      return;
    }

    // Create list item for adoption-info
    const listItem = document.createElement("li");

    const article = document.createElement("article");
    const typeParagraph = document.createElement("p");
    typeParagraph.textContent = `Pet: ${type}`;
    const genderParagraph = document.createElement("p");
    genderParagraph.textContent = `Gender: ${gender}`;
    const ageParagraph = document.createElement("p");
    ageParagraph.textContent = `Age: ${age}`;

    article.appendChild(typeParagraph);
    article.appendChild(genderParagraph);
    article.appendChild(ageParagraph);
    listItem.appendChild(article);

    const buttonsDiv = document.createElement("div");
    buttonsDiv.classList.add("buttons");

    const editBtn = document.createElement("button");
    editBtn.classList.add("edit-btn");
    editBtn.textContent = "Edit";
    buttonsDiv.appendChild(editBtn);

    const doneBtn = document.createElement("button");
    doneBtn.classList.add("done-btn");
    doneBtn.textContent = "Done";
    buttonsDiv.appendChild(doneBtn);

    listItem.appendChild(buttonsDiv);
    adoptionInfo.appendChild(listItem);

    // Clear input fields
    typeInput.value = "";
    ageInput.value = "";
    genderInput.value = "";

    // Edit button functionality
    editBtn.addEventListener("click", () => {
      typeInput.value = type;
      ageInput.value = age;
      genderInput.value = gender;
      adoptionInfo.removeChild(listItem);
    });

    // Done button functionality
    doneBtn.addEventListener("click", () => {
      adoptionInfo.removeChild(listItem);
      buttonsDiv.removeChild(editBtn);
      buttonsDiv.removeChild(doneBtn);

      const clearBtn = document.createElement("button");
      clearBtn.classList.add("clear-btn");
      clearBtn.textContent = "Clear";
      buttonsDiv.appendChild(clearBtn);

      adoptedList.appendChild(listItem);

      // Clear button functionality
      clearBtn.addEventListener("click", () => {
        adoptedList.removeChild(listItem);
      });
    });
  });
}

solve();
