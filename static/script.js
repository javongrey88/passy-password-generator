function togglePassword() {
    const pwd = document.getElementById("password");
    pwd.type = pwd.type === "password" ? "text" : "password";
}

function copyPassword() {
    const pwd = document.getElementById("password");
    navigator.clipboard.writeText(pwd.value).then(() => {
        alert("Password copied to clipboard!");
    });
}