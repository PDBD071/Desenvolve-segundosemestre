//arrow function
const Soma = (num1, num2) => num1 + num2
const Subtrai = (num1, num2) => num1 - num2
const Multiplica = (num1, num2) => num1 * num2
const Divide = (num1, num2) => num1 / num2

const MostraResultado =(num1, num2) =>{
    console.log(`Soma entre ${num1} e ${num2}`, Soma(num1, num2));
    console.log(`Diferença entre ${num1} e ${num2}`, Subtrai(num1, num2));
    console.log(`Produto entre ${num1} e ${num2}` , Multiplica(num1, num2));
    console.log(`Quociente de ${num1} e ${num2}` , Divide(num1, num2));
}

MostraResultado(10, 2);

//function
function soma(num1, num2) {
    return num1 + num2;
  }
  
  function subtrai(num1, num2) {
    return num1 - num2;
  }
  
  function multiplica(num1, num2) {
    return num1 * num2;
  }
  
  function divide(num1, num2) {
    return num1 / num2;
  }
  
  function mostraResultado(num1, num2) {
    console.log(`[Soma] entre ${num1} e ${num2}:`, soma(num1, num2));
    console.log(`[Subtração] entre ${num1} e ${num2}:`, subtrai(num1, num2));
    console.log(`[Multiplicação] entre ${num1} e ${num2}:`, multiplica(num1, num2));
    console.log(`[Divisão] entre ${num1} e ${num2}:`, divide(num1, num2));
  }
  
  MostraResultado(10, 5);