document.addEventListener("DOMContentLoaded", () => {
  fetch('/api/dividends')
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("dividendsList");
      data.forEach(d => {
        const li = document.createElement("li");
        li.className = "border-b pb-2";
        li.textContent = `📅 ${d.date} — 🏢 ${d.company} — 💸 ${d.amount} €`;
        list.appendChild(li);
      });

      // Graphique
      const ctx = document.getElementById('dividendChart').getContext('2d');
      const chartData = {
        labels: data.map(d => d.date),
        datasets: [{
          label: 'Dividendes (€)',
          data: data.map(d => d.amount),
        }]
      };
      new Chart(ctx, {
        type: 'bar',
        data: chartData
      });
    });
});
