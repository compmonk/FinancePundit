let stocks = [];
let stockVolumes = [];

function initDropdown() {
    if (localStorage.getItem("stocks") === null) {
        $.getJSON("/api/stocks", function (data) {
            stocks = data;
            console.log(stocks);
            localStorage.setItem('stocks', JSON.stringify(stocks));
            $('.stock').select2({
                placeholder: "Please select a Stock",
                data: data.map(function (stock) {
                    return {
                        'text': stock.symbol + "(" + stock.name.slice(0, 30) + ")",
                        'id': stock.id
                    }
                })
            });
        });
    } else {
        stocks = JSON.parse(localStorage.getItem('stocks'));
        console.log(stocks);
        $('.stock').select2({
            placeholder: "Please select a Stock",
            data: stocks.map(function (stock) {
                return {
                    'text': stock.symbol + "(" + stock.name.slice(0, 30) + ")",
                    'id': stock.id
                }
            })
        });
    }

}

initDropdown();

function addStock() {
    initDropdown();
    stockVolumes.push({
        "stock": stocks.filter(function (stock) {
            return stock.id === document.getElementById('stock').value
        })[0],
        "volume": document.getElementById('volume').value
    });
    $('#stock-volume tr:last').after(`<tr><td>${stockVolumes[stockVolumes.length - 1]['stock'].symbol}</td><td>${stockVolumes[stockVolumes.length - 1].volume}</td></tr>`);
    console.log({
        stockVolumes
    });
    document.getElementById('stock').value = null;
    document.getElementById('volume').value = 0
}

function submitStockVolumes(userId) {
    $.ajax({
        'url': `/auth/${userId}`,
        'ype': 'PUT',
        'data': stockVolumes,
        'success': function (data) {
            $(location).attr('href', '/dashboard/')
        }
    })
}