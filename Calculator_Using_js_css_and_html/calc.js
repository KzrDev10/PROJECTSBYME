// calc code

const display = document.getElementById("display");
// bc diplay already empty function appendtodisplay adds things there
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
