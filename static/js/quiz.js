var currentQuestion = 0;
var score = 0;
var totQuestions = allquestions.length;

var container = document.getElementById('Quizcontainer');
var questionEl = document.getElementById('question');
var opt1 = document.getElementById('opt1');
var opt2 = document.getElementById('opt2');
var opt3 = document.getElementById('opt3');
var opt4 = document.getElementById('opt4');
var nextButton = document.getElementById('nextButton');
var go3 = document.getElementById('letsgo3');
var resultCont = document.getElementById('result');
var go = document.getElementById('letsgo');
var go1 = document.getElementById('letsgo1');
var go2 = document.getElementById('letsgo2');
var msg = document.getElementById('msg');
var ans1 = document.getElementById('ans1');
var ans2 = document.getElementById('ans2');
var ans3 = document.getElementById('ans3');
var ans4 = document.getElementById('ans4');
var ans5 = document.getElementById('ans5');
var answerCont = document.getElementById('answers');



function loadQuestion(questionIndex) {
	var q = allquestions[questionIndex];
	questionEl.textContent = (questionIndex + 1) + '. '+ q.question;
	opt1.textContent = q.option1;
	opt2.textContent = q.option2;
	opt3.textContent = q.option3;
	opt4.textContent = q.option4;
}
function loadNextQuestion() {
	var selectedOption = document.querySelector('input[type=radio]:checked');//to check if the answer is selected by user
	if(!selectedOption) {
		alert('Please select your answer');
		return;
	}
	var answer = selectedOption.value;
	if(allquestions[currentQuestion].answer == answer) {//to check if the answer is correct
		score += 10;
	}
	selectedOption.checked = false;
	currentQuestion++;
	if(currentQuestion == totQuestions - 1) { //change the content of NEXT button to FINISH for the last question 
		nextButton.textContent = 'Finish';
	}
	if(currentQuestion == totQuestions) {//display the score after finishing all questions
		container.style.display = 'none';
		resultCont.style.display = '';
		resultCont.textContent = 'Your score: ' + score;
		
		for(i=0; i<totQuestions-1;i++) {

		}
		// printAnswer(allquestions[0]);
		if(score == 50) {
			go.style.display = '';
		} else if(score <= 20) {
			msg.style.display = '';
			go3.style.display = '';
		} else if(score < 40) {
			go2.style.display = '';
		} else  {
			go1.style.display = '';
		} 
		//go.style.display = '';
		
		return;
	}
	loadQuestion(currentQuestion);
}

loadQuestion(currentQuestion);
