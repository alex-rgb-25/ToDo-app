
// listen for click events. only todos have the clickable class
//then toggle on/off the del class
document.addEventListener("click", function(e){
    let target = e.target
    
    if(target.classList.contains("clickable")){
        if(target.classList.contains("del")){
            target.classList.remove("del")
        } else{
            target.classList.add("del")
        }
    }
 
    
})