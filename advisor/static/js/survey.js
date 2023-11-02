form = document.getElementById("form")

// alert("Hellow world")

form.addEventListener('submit', (e) => {
    const usersInputs = []

    usersInputs.push(document.getElementById("database").value)
    usersInputs.push(document.getElementById("architecture").value)
    usersInputs.push(document.getElementById("computing").value)
    usersInputs.push(document.getElementById("security").value)
    usersInputs.push(document.getElementById("networking").value)
    usersInputs.push(document.getElementById("developement").value)
    usersInputs.push(document.getElementById("skills").value)
    usersInputs.push(document.getElementById("management").value)
    usersInputs.push(document.getElementById("forensics").value)
    usersInputs.push(document.getElementById("tech_comm").value)
    usersInputs.push(document.getElementById("ai").value)
    usersInputs.push(document.getElementById("soft_eng").value)
    usersInputs.push(document.getElementById("business").value)
    usersInputs.push(document.getElementById("comm").value)
    usersInputs.push(document.getElementById("data").value)
    usersInputs.push(document.getElementById("troub").value)
    usersInputs.push(document.getElementById("graphics").value)

    console.log(usersInputs)

    flag = new Boolean(false);

    // console.log(flag)

    // if(usersInputs.length > 17){
    //     flag = true;
    // }
    for(var i = 0; i < 17; i++){
        console.log(usersInputs[i])
        if(usersInputs[i] != "Not Interested"){
            flag = true;
            break;
        }
    }
    if(flag == false){
        // console.log(flag)
        alert("Please select the kills you know.. ")
        e.preventDefault()
    }
    else{
        // alert("I am here")
        console.log(flag)
    }
})