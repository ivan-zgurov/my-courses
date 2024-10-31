window.addEventListener("load", solve);

function solve() {
  const nameInput = document.getElementById('name');
  const phoneInput = document.getElementById('phone');
  const categoryInput = document.getElementById('category');
  const addBtn = document.getElementById('add-btn');
  const checkList = document.getElementById('check-list');
  const contactList = document.getElementById('contact-list');

  addBtn.addEventListener('click', () => {
    const name = nameInput.value.trim();
    const phone = phoneInput.value.trim();
    const category = categoryInput.value;

    if (!name || !phone || !category) {
      return;
    }

    // Create new list item for check-list
    const listItem = document.createElement('li');

    const article = document.createElement('article');
    const nameParagraph = document.createElement('p');
    nameParagraph.textContent = `name:${name}`;
    const phoneParagraph = document.createElement('p');
    phoneParagraph.textContent = `phone:${phone}`;
    const categoryParagraph = document.createElement('p');
    categoryParagraph.textContent = `category:${category}`;

    article.appendChild(nameParagraph);
    article.appendChild(phoneParagraph);
    article.appendChild(categoryParagraph);
    listItem.appendChild(article);

    const buttonsDiv = document.createElement('div');
    buttonsDiv.classList.add('buttons');

    const editBtn = document.createElement('button');
    editBtn.classList.add('edit-btn');
    editBtn.textContent = 'Edit';
    buttonsDiv.appendChild(editBtn);

    const saveBtn = document.createElement('button');
    saveBtn.classList.add('save-btn');
    saveBtn.textContent = 'Save';
    buttonsDiv.appendChild(saveBtn);

    listItem.appendChild(buttonsDiv);
    checkList.appendChild(listItem);

    // Clear input fields
    nameInput.value = '';
    phoneInput.value = '';
    categoryInput.value = '';

    // Edit button functionality
    editBtn.addEventListener('click', () => {
      nameInput.value = name;
      phoneInput.value = phone;
      categoryInput.value = category;
      checkList.removeChild(listItem);
    });

    // Save button functionality
    saveBtn.addEventListener('click', () => {
      checkList.removeChild(listItem);
      buttonsDiv.removeChild(editBtn);
      buttonsDiv.removeChild(saveBtn);

      const deleteBtn = document.createElement('button');
      deleteBtn.classList.add('del-btn');
      deleteBtn.textContent = 'Delete';
      listItem.appendChild(deleteBtn);

      contactList.appendChild(listItem);

      // Delete button functionality
      deleteBtn.addEventListener('click', () => {
        contactList.removeChild(listItem);
      });
    });
  });
}

solve();
