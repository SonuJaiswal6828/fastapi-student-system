const API = "http://127.0.0.1:8000/students"

async function addStudent(){
    let name = document.getElementById('name').value;
    let age = document.getElementById('age').value;
    let marks = document.getElementById('marks').value;

    if(!name|| !age|| !marks ){
        alert('Please fil all fields')
    }

    const res =await fetch(API, {
        method:'POST',
        headers:{"Content-Type": "application/json"},
        body : JSON.stringify({name, age, marks})
    });
    const data = await res.json();
    document.getElementById('output').textContent = JSON.stringify(data, null, 2)
}



function details(student) {
    const tableBody = document.getElementById('studentsTableBody');
    const row = document.createElement('tr');

    row.innerHTML = `
        <td>${student[0]}</td>
        <td>${student[1]}</td>
        <td>${student[2]}</td>
        <td>${student[3]}</td>
        <td>${student[4]}</td>
    `;

    tableBody.appendChild(row);
}

async function getStudents() {
    const res = await fetch(API)
    const data = await res.json();
    
    console.log(data)
    const tableBody = document.getElementById('studentsTableBody');
    tableBody.innerHTML = '';

    data.Students.forEach(element => {
        details(element)
    });
}

async function deleteStudent(){
    const studentId = document.getElementById('deleteId').value; 
    const res = await fetch(`${API}/${studentId}`, {
        method:'DELETE',
        headers:{"Content-Type":"application/json"}
    });
    const data = await res.json();
    console.log(data)
}



