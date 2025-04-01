const body = document.body;
body.addEventListener('mouseup', ()=>{
    var selection = window.getSelection()
    var selected = selection.toString();
    if(!selected) return;

    const range = selection.getRangeAt(0);
    const startContainer = range.startContainer;
    const endContainer = range.endContainer;

    const startElement = startContainer.nodeType === Node.TEXT_NODE 
        ? startContainer.parentElement.getAttribute('id')
        : startContainer.getAttribute('id');

    const endElement = endContainer.nodeType === Node.TEXT_NODE 
        ? endContainer.parentElement.getAttribute('id')
        : endContainer.getAttribute('id');
    
    if (!(startElement && endElement)){
        alert('к сожалению слово которое выделено нельзя занести в базу данных');
    }
    else{
        var mas = [];
        let words = '';
        for(let i = parseInt(startElement); i <= parseInt(endElement); i++){
            mas.push(document.getElementById(String(i)).textContent);
        };
        for (i of mas){
            words = words + i + ' ';
        }
        var add = document.getElementById('add');
        if (add){
          console.log(add);
          add.remove();
        };
        
        // Создаем модалку на лету
        const modalHTML = `
          <div class = "fixed-bottom bg-dark border border-light p-2 m-3 text-white rounded-3" id = "add" style = "width:30%">
            <form method = "post">
              ${csrf_token}
              <legend class = "border border-dark px-3 rounded" style = "width:fit-content">Перевод к ${words}</legend>
              <input type="text" class="bg-dark form-control text-white form-label" name ="trans">
              <button type="button" class="position-absolute top-0 end-0 btn-close btn-close-white p-2" aria-label="Закрыть"></button>
              <input type="hidden" name ="id_start_word" value = "${startElement}">
              <input type="hidden" name ="id_end_word" value = "${endElement}">
              <input type="hidden" name ="words" value = "${words}">
              <button name="title" value = "${title}" class = "btn btn-dark p-3" type="submit">Отправить</button>
            </form>
            
          </div>
        `;
        
        document.body.insertAdjacentHTML('afterbegin', modalHTML);
        var kr = document.querySelector('.btn-close');
        var add = document.getElementById('add');
        selection.removeAllRanges()
        // Закрытие при клике на крестик
        kr.addEventListener('click', () => {
            
            add.remove();
            

        });

        
    };
});