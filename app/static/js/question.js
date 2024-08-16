class Questionnaire {
    constructor(questions) {
        this.questions = questions; // 質問の配列
        this.currentQuestionIndex = 0; // 現在の質問のインデックス
        this.inputValues = []; // 入力された値を保持する配列
        this.questionsContainer = document.getElementById('questions-container'); // 質問を表示するコンテナ
        this.nextButton = document.getElementById('next-button'); // 次へボタン
        this.finishMessage = document.getElementById('finish-message'); // 終了メッセージ

        this.showQuestion(this.currentQuestionIndex); // 最初の質問を表示
    }

    // 質問を表示するメソッド
    showQuestion(index) {
        this.questionsContainer.innerHTML = ''; // コンテナをクリア

        // 新たなdiv要素を作成（グループ化するため）
        const questionDiv = document.createElement('div');
        questionDiv.className = 'question';

        // 新たなlabel要素を作成（質問文を表示するため）
        const questionLabel = document.createElement('label');
        questionLabel.textContent = this.questions[index];
        questionLabel.setAttribute('for', `answer-${index}`);

        // 新たなinput要素を作成（回答を入力するため）
        const questionInput = document.createElement('input');
        questionInput.type = 'text';
        questionInput.id = `answer-${index}`;
        questionInput.name = `answer-${index}`;

        // div要素に追加
        questionDiv.appendChild(questionLabel);
        questionDiv.appendChild(document.createElement('br'));
        questionDiv.appendChild(questionInput);
        this.questionsContainer.appendChild(questionDiv);
    }

    // 次の質問に進むメソッド
    showNextQuestion() {
        const currentInput = document.getElementById(`answer-${this.currentQuestionIndex}`);
        this.inputValues[this.currentQuestionIndex] = currentInput.value;

        this.currentQuestionIndex++;
        if (this.currentQuestionIndex < this.questions.length) {
            this.showQuestion(this.currentQuestionIndex);
        } else {
            this.showFinishMessage();
        }
    }

    // 終了メッセージを表示するメソッド
    showFinishMessage() {
        console.log("ユーザーが入力した値: ", this.inputValues); // 全ての入力値を表示
        this.nextButton.style.display = 'none'; // 次へボタンを隠す
        this.finishMessage.style.display = 'block'; // 終了メッセージを表示
    }
}

// 質問の配列を定義
const questions = [
    "質問1: お名前は？",
    "質問2: 年齢は？",
    "質問3: 趣味は？",
];

// Questionnaireクラスのインスタンスを作成
const questionnaire = new Questionnaire(questions);

// 次へボタンのクリックイベントリスナーを追加
document.getElementById('next-button').addEventListener('click', () => {
    questionnaire.showNextQuestion();
});