// calc code

const display = document.getElementById("display");

function appendToDisplay(input){
    display.value += input;
}

function calculate(){
    try{

        // eval function is basically a built in calulator so it reads what you type and solves it
        

        display.value = eval(display.value)
    }
    catch(error){
        display.value = "error";
    }
}
function clearDisplay(){
    display.value = "";
}