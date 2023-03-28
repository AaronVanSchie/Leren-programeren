const kleuren = ["red","purple","blue","black"];
let index = 0

for(let i = 1; i< 30 + 1; i++){
    const div = document.createElement('button');
    div.textContent = i

div.addEventListener('click', function Onclick() {
    div.style.backgroundColor = kleuren[index];
    if (index in kleuren){
        index = index + 1
    } else if (!(index in kleuren)) {
        index = index - 4
    }
  });
    container.appendChild(div)
}