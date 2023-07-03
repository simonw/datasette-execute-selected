let fragmentsChecked = new Map();

async function checkFragment(fragment) {
    if (fragmentsChecked.has(fragment)) {
        return fragmentsChecked.get(fragment);
    }
    // Send to backend to check if it's a valid query fragment
    const response = await fetch('/-/validate-query-selection', {
        method: 'POST',
        body: JSON.stringify({query: fragment}),
        headers: {
            'Content-Type': 'application/json',
        }
    });
    const data = await response.json();
    fragmentsChecked.set(fragment, data.valid);
    return data.valid;
}

setInterval(async () => {
    const hideButton = () => {
        const btn = document.querySelector('.execute-selected-query');
        if (btn) {
            btn.style.display = 'none';
        }
    };
    const editor = this.editor;
    if (!editor) {
        hideButton();
        return;
    }
    const selection = editor.state.sliceDoc(editor.state.selection.main.from, editor.state.selection.main.to)
    if (!selection || selection.length === 0) {
        hideButton();
        return;
    }
    const isValid = await checkFragment(selection);
    if (isValid) {
        // Show the "Execute selected query" button
        const btn = document.querySelector('.execute-selected-query');
        if (!btn) {
            // Create it
            const btn = document.createElement('button');
            btn.setAttribute('type', 'button');
            btn.classList.add('execute-selected-query');
            btn.innerText = 'Execute selected SQL';
            btn.addEventListener('click', async () => {
                alert('TODO: implement this');
            });
            document.querySelector('#sql-format').parentNode.appendChild(btn);
        } else {
            btn.style.display = 'inline';
        }
    } else {
        hideButton();
    }
}, 1000);
