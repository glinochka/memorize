data = JSON.parse(data);
var  title = data.title;
var transles = data.transles;
var many_transles = data.many_transles;
var last_id = data.last_trans

console.log(data)
for (info of transles){
  let w = document.getElementById(String(info[0]));
  w.style.color = 'red';
  w.style.textDecoration = 'underline';
  w.setAttribute('title', info[1]);
};

for (info of many_transles){
    for (let i = info[0]; i<= info[1]; i++){
        console.log(i);
        let w = document.getElementById(String(i));
        w.style.color = 'red';
        w.style.textDecoration = 'underline';
        w.setAttribute('title', info[2]);
    }
};
console.log(document.getElementById(last_id));
document.getElementById(last_id).scrollIntoView({ behavior: "smooth", block: "center" });