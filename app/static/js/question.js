class Questionnaire {
    constructor(standardQuestions, customQuestionsNum) {
        this.standardQuestions = standardQuestions; // 質問の配列
        this.standardQuestionsInput = []; // 入力された値を保持する配列
        this.customQuestionsNum = customQuestionsNum; // 追加質問の数
        this.customQuestions = []; // 追加質問の配列
        this.customQuestionsInput = []; // 追加質問の入力値を保持する配列

        this.currentQuestionIndex = 0; // 現在の質問のインデックス

        this.questionsContainer = document.getElementById('questions-container'); // 質問を表示するコンテナ
        this.nextButton = document.getElementById('next-button'); // 次へボタン
        this.finishMessage = document.getElementById('finish-message'); // 終了メッセージ

        this.showStandardQuestion(this.currentQuestionIndex); // 最初の質問を表示
    }

    // 質問を表示するメソッド
    showStandardQuestion(index) {
        this.questionsContainer.innerHTML = ''; // コンテナをクリア

        // 新たなdiv要素を作成（グループ化するため）
        const questionDiv = document.createElement('div');
        questionDiv.className = 'question';

        // 新たなlabel要素を作成（質問文を表示するため）
        const questionLabel = document.createElement('label');
        questionLabel.textContent = this.standardQuestions[index];
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

    showCustomQuestion(customIndex) {
        this.questionsContainer.innerHTML = ''; // コンテナをクリア

        const questionDiv = document.createElement('div');
        questionDiv.className = 'custom-question';

        const questionLabel = document.createElement('label');
        questionLabel.textContent = `新しい質問${customIndex + 1}:`;
        questionLabel.setAttribute('for', `custom-question-${customIndex}`);

        const questionInput = document.createElement('input');
        questionInput.type = 'text';
        questionInput.id = `custom-question-${customIndex}`;
        questionInput.name = `custom-question-${customIndex}`;

        const answerLabel = document.createElement('label');
        answerLabel.textContent = `回答${customIndex + 1}:`;
        answerLabel.setAttribute('for', `custom-answer-${customIndex}`);

        const answerInput = document.createElement('input');
        answerInput.type = 'text';
        answerInput.id = `custom-answer-${customIndex}`;
        answerInput.name = `custom-answer-${customIndex}`;

        questionDiv.appendChild(questionLabel);
        questionDiv.appendChild(document.createElement('br'));
        questionDiv.appendChild(questionInput);
        questionDiv.appendChild(document.createElement('br'));
        questionDiv.appendChild(answerLabel);
        questionDiv.appendChild(document.createElement('br'));
        questionDiv.appendChild(answerInput);

        this.questionsContainer.appendChild(questionDiv);
    }


    // 次の質問に進むメソッド
    showNextQuestion() {
        // 通常の質問時
        if (this.currentQuestionIndex < this.standardQuestions.length) {
            // 入力された値を取得し，保存
            const currentInput = document.getElementById(`answer-${this.currentQuestionIndex}`);
            this.standardQuestionsInput.push(currentInput.value);

            this.currentQuestionIndex++;

            // 次の質問がある場合
            if (this.currentQuestionIndex < this.standardQuestions.length) {
                // 次の質問を表示
                this.showStandardQuestion(this.currentQuestionIndex);
            }
            else {
                // 最初の追加質問を表示
                this.showCustomQuestion(0);
            }
        // 追加質問時
        } else {
            // 入力された値を取得し，保存
            const customIndex = this.currentQuestionIndex - this.standardQuestions.length;
            const customQuestion = document.getElementById(`custom-question-${customIndex}`);
            const customAnswer = document.getElementById(`custom-answer-${customIndex}`);
            this.customQuestions.push(customQuestion.value);
            this.customQuestionsInput.push(customAnswer.value);

            this.currentQuestionIndex++;

            if (this.currentQuestionIndex - this.standardQuestions.length < this.customQuestionsNum) {
                this.showCustomQuestion(this.currentQuestionIndex - this.standardQuestions.length);
            } else {
                this.showFinishMessage();
            }
        }
    }

    // 終了メッセージを表示するメソッド
    showFinishMessage() {
        // 入力値確認
        console.log("通常の質問: ", this.standardQuestions)
        console.log("ユーザーが入力した値: ", this.standardQuestionsInput); // 全ての入力値を表示
        console.log("ユーザーが入力した追加質問: ", this.customQuestions); // 全ての追加質問を表示
        console.log("ユーザーが入力した追加質問の回答: ", this.customQuestionsInput); // 全ての追加質問の回答を表示

        this.nextButton.style.display = 'none'; // 次へボタンを隠す
        this.finishMessage.style.display = 'block'; // 終了メッセージを表示
    }
}

// 質問の配列を定義
const STANDARD_QUESTIONS = [
    "name",
    "age",
    "country",
    "favorite things",
    "mbti"
];

const CUSTOM_QUESTIONS_NUM = 3;

// Questionnaireクラスのインスタンスを作成
const questionnaire = new Questionnaire(STANDARD_QUESTIONS, CUSTOM_QUESTIONS_NUM);

// 次へボタンのクリックイベントリスナーを追加
document.getElementById('next-button').addEventListener('click', () => {
    questionnaire.showNextQuestion();
});