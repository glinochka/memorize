var words = document.querySelectorAll('w');
words.forEach(w => {
    w.addEventListener('click', () => {
        var add = document.getElementById('add');
        if (add){
          add.remove();
        };
        
        const id = w.id;
        const word = w.textContent;
        // Создаем модалку на лету
        const modalHTML = `
          <div class = "fixed-bottom bg-dark border border-light p-2 m-3 text-white rounded-3" id = "add" style = "width:30%">
            <form method = "post">
              ${csrf_token}
              <legend class = "border border-dark px-3 rounded" style = "width:fit-content">Перевод к ${word}</legend>
              <input type="text" class="bg-dark form-control text-white form-label" name ="trans">
              <button type="button" class="position-absolute top-0 end-0 btn-close btn-close-white p-2" aria-label="Закрыть"></button>
              <input type="hidden" name ="id" value = "${id}">
              <input type="hidden" name ="word" value = "${word}">
              <button name="title" value = "${title}" class = "btn btn-dark p-3" type="submit">Отправить</button>
            </form>
            
          </div>
        `;
        
        document.body.insertAdjacentHTML('afterbegin', modalHTML);
        var kr = document.querySelector('.btn-close')
        var add = document.getElementById('add')
        // Закрытие при клике на крестик
        kr.addEventListener('click', () => {
          add.remove();
        });
      });
});
