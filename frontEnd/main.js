// Access the from the specified path
fetch("http://127.0.0.1:5001/list") 
    
    // Converting received data to JSON 
    .then(response => response.json()) 
    .then(json => { 
   
        // Create a variable to store HTML 
        let li = `<tr><th>Name</th></tr>`; 
        
        // Loop through each data and add a table row 
        json.forEach(user => { 
            li += `<tr> 
                <td>${user.name} </td> 
            </tr>`; 
        }); 
   
    // Display result 
    document.getElementById("users").innerHTML = li; 
}); //  GET request using fetch() 
