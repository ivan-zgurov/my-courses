// 80 / 100
window.addEventListener("load", solve);

function solve() {
  const playerInput = document.getElementById("player");
  const scoreInput = document.getElementById("score");
  const roundInput = document.getElementById("round");
  const addBtn = document.getElementById("add-btn");
  const sureList = document.getElementById("sure-list");
  const scoreboardList = document.getElementById("scoreboard-list");
  const clearBtn = document.querySelector(".btn.clear");

  addBtn.addEventListener("click", () => {
    const player = playerInput.value.trim();
    const score = scoreInput.value.trim();
    const round = roundInput.value.trim();

    if (!player || !score || !round) {
      return;
    }

    // Create new list item for sure-list
    const listItem = document.createElement("li");
    listItem.classList.add("dart-item");

    const article = document.createElement("article");
    const playerParagraph = document.createElement("p");
    playerParagraph.textContent = player;
    const scoreParagraph = document.createElement("p");
    scoreParagraph.textContent = `Score: ${score}`;
    const roundParagraph = document.createElement("p");
    roundParagraph.textContent = `Round: ${round}`;

    article.appendChild(playerParagraph);
    article.appendChild(scoreParagraph);
    article.appendChild(roundParagraph);
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
    sureList.appendChild(listItem);

    // Clear input fields and disable Add button
    playerInput.value = "";
    scoreInput.value = "";
    roundInput.value = "";
    addBtn.disabled = true;

    // Edit button functionality
    editBtn.addEventListener("click", () => {
      playerInput.value = player;
      scoreInput.value = score;
      roundInput.value = round;
      addBtn.disabled = false;
      sureList.removeChild(listItem);
    });

    // Ok button functionality
    okBtn.addEventListener("click", () => {
      sureList.removeChild(listItem);
      buttonsDiv.removeChild(editBtn);
      buttonsDiv.removeChild(okBtn);

      scoreboardList.appendChild(listItem);
      addBtn.disabled = false;
    });
  });

  // Enable Add button when input fields are changed
  [playerInput, scoreInput, roundInput].forEach((input) => {
    input.addEventListener("input", () => {
      addBtn.disabled =
        !playerInput.value.trim() ||
        !scoreInput.value.trim() ||
        !roundInput.value.trim();
    });
  });

  // Clear button functionality
  clearBtn.addEventListener("click", () => {
    location.reload();
  });
}

solve();
