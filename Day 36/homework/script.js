function computerChoice() {
    const choices = ['rock', 'paper', 'scissors'];
    const randomIndex = Math.floor(Math.random() * 3);
    return choices[randomIndex];
}

function determineWinner(user, computer) {
    if (user === computer) {
        return 'It\'s a tie!';
    } else if ((user === 'rock' && computer === 'scissors') ||
               (user === 'paper' && computer === 'rock') ||
               (user === 'scissors' && computer === 'paper')) {
        return 'You win!';
    } else {
        return 'You lose!';
    }
}

function userChoice(choice) {
    const computer = computerChoice();
    const result = determineWinner(choice, computer);

    const resultElement = document.getElementById('result');
    resultElement.textContent = `You chose ${choice}. | Computer chose ${computer}. | ${result}`;
}