# **Javascript Event Listeners**
- calls a function when a certain event occurs

---

# **onclick**

```
<head>
    <script>

        let counter = 0;

        function count() 
        {
            counter++;
            document.querySelector('h2').innerHtml = counter
            if(counter % 10===0) { alert(`Count is now ${counter}`); }
        } 

        function hello() 
        {
            const heading = document.querySelector('h1');
            if (heading.innerHTML === 'Hello!') heading.innerHTML = 'Goodbye!';
            else heading.innerHTML = 'Hello!';
        }
    ...

===========================================
<body>
    <h1>Hello</h1>

    <h2>0</h2>
    <button onclick="count()">Click Here</button>
</body>
```

---

# **Manipulating the DOM**
- debug using inspect -> console 

**Event Listeners**
```
    <script>
    function count() {...}
    document.addEventListener('DOMContentLoaded', funcion() {
        document.querySelector('button').onclick = count;
    });
    ...
    <body>
        <h2>0</h2>
        <button>Count</button>
```

---

Good practice to move javascript code to seperate file
- code can be resued over multiple different pages 
```
    <script src="counter.js"></script>
```

---

# **Forms**


```
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            document.querySelector('form').onsubmit = function() {
                const name = document.querySelector('#name').value;
                alert(`Hello, #{name});
            };
        });
    ...
==========================================================
    <body>
        <form>
            <input id="name" type="text">
            <input type="submit>
        ...
```

---

# **Accesing CSS Properties**

```
    document.addEventListener('DOMContentLoaded, () => {
        document.querySelector('select').onchange = function() 
        {
            document.querySelector('#hello').style.color = this.value;
        }
        ...
    });

==========================================================

    <h1 id="hello>Hello!</h1>
    <select>
        <option value="black">Black</option>
        <option value="red">Red</option>
        <option value="blue">Blue</option>
        <option value="green">Green</option>
    </select>
```
---
# **Editing Document Body**
```
    document.addEventListener('DOMContentLoaded', function() {

        // By default, submit button is disabled
        document.querySelector('#submit').disabled = true;

        document.querySelector('#task').onkeyup = () => {
            if (document.querySelector('#task').value.length > 0)
            {
                document.querySelector('#submit').disabled = false;
            }
            else
            {
                document.querySelector('#submit').disabled = true;
            }
        }

        document.querySelector('form').onsubmit = () => {
            const task = document.querySelector('#task').value;
            console.log(task);

            const li = document.createElement('li);
            li.innerHTML = task;

            document.querySelector('#tasks').append(li);
            document.querySelector('#task').value = '';

            document.querySelector('#submit').disabled = true;

            // Stop form from submitting
            return false;
        }
    });
============================================================

    <form>
        <input id="task" type="text">
        <input id="submit" type="submit">
    </form>
```
---
# **Intervals**

```
    function count() {...}
    document.addEventListener('DOMContentLoaded', funcion() {
        document.querySelector('button').onclick = count;

        // Runs count function every 1000 mls
        setInterval(count, 1000);
    });

```
---
# **Local Storage**

+ localStorage.getItem(key)
+ localStorage.setItem(key, value)

```
    if (!localStorage.getItem('counter')) {
        locatStorage.setItem('counter', 0);
    }

    function() count() 
    {
        let counter = localStorage.getItem('counter');
        counter++;
        document.querySelector('h1').innerHTML = counter;
        localStorage.setItem('counter', counter);
    }

```

# **API**

- structured way for one application to communicate with another service
    - data is typically transfered in JSON format (Javascript Object Notation)

```
document.addEventListener("DOMContentLoaded', function() {

    document.querySelector('form').onsubmit = function() {
        fetch('https://api.exchangeratesapi.io/latest?base=USD').then(response => response.json()).then(data => {
        const currency = document.querySelector('#currency').value;
        const rate = data.rates[currency];
        if (rate !== undefined) {
            document.querySelector('body').innerHTML = `1 USD is equal to ${rate.toFixed(3)} EUR.`;
        }
    });
    return false;
    }
});

=======================================================

<form>
    <input id="currency type="text">
    <input type="submit" value="Convert">
</form>
<div id="result">
</div>
```