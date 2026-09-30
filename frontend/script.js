const API_URL = "http://127.0.0.1:8000/expense_tracker_app";


async function addExpense() {

    const title = document.getElementById("addTitle").value;
    const amount = document.getElementById("addAmount").value;
    const category = document.getElementById("addCategory").value;

    const response = await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title,
            amount: Number(amount),
            category: category
        })
    });

    const data = await response.json();

    console.log(data);

    if (!response.ok) {
        showResult(data);
        return;
    }

    showResult(data);

    document.getElementById("addTitle").value = "";
    document.getElementById("addAmount").value = "";
    document.getElementById("addCategory").value = "";
}


async function getExpense() {

    const id = document.getElementById("getId").value;

    const response = await fetch(`${API_URL}/${id}`);

    const data = await response.json();

    showResult(data);
}


async function updateExpense() {

    const id = document.getElementById("updateId").value;

    const title = document.getElementById("updateTitle").value;
    const amount = document.getElementById("updateAmount").value;
    const category = document.getElementById("updateCategory").value;

    const response = await fetch(`${API_URL}/${id}`, {
        method: "PUT",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            title: title,
            amount: Number(amount),
            category: category
        })
    });

    const data = await response.json();

    showResult(data);
}


async function getAllExpenses() {

    const response = await fetch(API_URL);

    const data = await response.json();

    showResult(data);
}

function showResult(data) {
    const result = document.getElementById("result");

    // Error response
    if (data.detail) {
        result.innerHTML = `
            <p class="no-result">
                ${data.detail}
            </p>
        `;
        return;
    }

    // Multiple expenses
    if (Array.isArray(data)) {

        if (data.length === 0) {
            result.innerHTML = `
                <p class="no-result">
                    No expenses found.
                </p>
            `;
            return;
        }

        result.innerHTML = data.map(expense => `
            <div class="expense-item">

                <div class="expense-id">
                    Expense #${expense.id}
                </div>

                <div class="expense-title">
                    ${expense.title}
                </div>

                <div class="expense-amount">
                    ₹${expense.amount}
                </div>

                <div class="expense-info">
                    <span class="expense-label">Category</span>
                    <span class="category">
                        ${expense.category}
                    </span>
                </div>

                <div class="expense-info">
                    <span class="expense-label">Date</span>
                    <span class="expense-value">
                        ${expense.expense_date || "N/A"}
                    </span>
                </div>

                <div class="expense-actions">
                    <button
                        class="update-btn"
                        onclick="loadUpdateData(${expense.id})">
                        Update
                    </button>

                    <button
                        class="delete-btn"
                        onclick="deleteExpense(${expense.id})">
                        Delete
                    </button>
                </div>

            </div>
        `).join("");

        return;
    }

    // Single expense
    const expense = data.expense || data;

    result.innerHTML = `
        <div class="expense-item">

            <div class="expense-id">
                Expense #${expense.id}
            </div>

            <div class="expense-title">
                ${expense.title}
            </div>

            <div class="expense-amount">
                ₹${expense.amount}
            </div>

            <div class="expense-info">
                <span class="expense-label">Category</span>
                <span class="category">
                    ${expense.category}
                </span>
            </div>

            <div class="expense-info">
                <span class="expense-label">Date</span>
                <span class="expense-value">
                    ${expense.expense_date || "N/A"}
                </span>
            </div>

            <div class="expense-actions">
                <button
                    class="update-btn"
                    onclick="loadUpdateData(${expense.id})">
                    Update
                </button>

                <button
                    class="delete-btn"
                    onclick="deleteExpense(${expense.id})">
                    Delete
                </button>
            </div>

        </div>
    `;
}