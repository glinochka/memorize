function add_form(data){
  fetch(train,{
    method: 'POST',
    headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value},
    body: data
  }).then(res => res.json())
    .then(json => {
      var div_form = document.getElementById('train_form');
        if (div_form){
          div_form.remove();
        };
      const mess = json.mess;
      const words = json.words;
      const is_word = json.is_word;
      const train_form = `
        <div class = "text-white text-center d-flex flex-column align-items-center" id = "train_form">
          <p> Тренировка </p>
            <div class = "bg-dark p-2 text-white border border-white rounded" id = "add" style = "width:30%">
                <form method = "get" id ="form">
                  <legend class = "border border-dark px-3 rounded text-primary text-center" >${words.words}</legend>
                  <input type="text" class="bg-dark form-control text-white form-label" name ="trans">
                  <input type="hidden" name ="article" value="${words.article}">
                  <input type="hidden" name ="is_word" value="${is_word}">
                  <input type="hidden" name="words" value = "${words.st_words}">
                  <button  class = "btn btn-dark p-3" type="submit">Отправить</button>
                </form>
              </div>
        </div>
      `
      const word_train = document.getElementById('word_train');
      word_train.insertAdjacentHTML('afterbegin', train_form);
      var div_form = document.getElementById('train_form');

      if(mess){
        div_form.insertAdjacentHTML('beforeend',`<p class="text-danger m-3">${mess}</p>`);
      } else{
        div_form.insertAdjacentHTML('beforeend',`<p class="text-success m-3">Правильно!</p>`);
      };
      const form = document.getElementById('form');
      form.addEventListener('submit',(ev)=>{
        ev.preventDefault();
        const formData = new FormData(form);
        add_form(formData);
      });
    });
};
add_form('');



