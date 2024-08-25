import { CameraHandler } from "./cameraHandler.js";

class Questionnaire {
    constructor(standardQuestions, customQuestionsNum, groupName) {
        this.standardQuestions = standardQuestions; // 質問の配列
        this.standardQuestionsInput = []; // 入力された値を保持する配列
        this.customQuestionsNum = customQuestionsNum; // 追加質問の数
        this.customQuestions = []; // 追加質問の配列
        this.customQuestionsInput = []; // 追加質問の入力値を保持する配列
        this.groupName = groupName; // グループ名

        this.currentQuestionIndex = 0; // 現在の質問のインデックス

        this.questionsContainer = document.getElementById('questions-container'); // 質問を表示するコンテナ
        this.nextButton = document.getElementById('next-button'); // 次へボタン
        this.finishMessage = document.getElementById('finish-message'); // 終了メッセージ
        this.cameraContainer = document.getElementById('camera-container'); // カメラキャプチャ画面

        this.cameraHandler = new CameraHandler('video', 'canvas', 'captured-image'); // カメラハンドラーのインスタンスを作成

        this.showStandardQuestion(this.currentQuestionIndex); // 最初の質問を表示
    }

    // 質問を表示するメソッド
    showStandardQuestion(index) {
        this.questionsContainer.innerHTML = ''; // コンテナをクリア

        if (this.standardQuestions[index] === 'image') {
            this.showCameraCapture();
        } else if (this.standardQuestions[index] === 'country') {
            this.selectCountry(index);
        } else {
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
    }

    showCustomQuestion(customIndex) {
        this.questionsContainer.innerHTML = ''; // コンテナをクリア
        this.cameraContainer.innerHTML = ''; // カメラコンテナをクリア
        this.cameraContainer.style.display = 'none'; // カメラコンテナを隠す

        // 新たなdiv要素を作成（グループ化するため）
        const questionDiv = document.createElement('div');
        questionDiv.className = 'custom-question';

        // 新たなlabel要素を作成（質問文を表示するため）
        const questionLabel = document.createElement('label');
        questionLabel.textContent = `新しい質問${customIndex + 1}:`;
        questionLabel.setAttribute('for', `custom-question-${customIndex}`);

        // 新たなinput要素を作成（質問を入力するため）
        const questionInput = document.createElement('input');
        questionInput.type = 'text';
        questionInput.id = `custom-question-${customIndex}`;
        questionInput.name = `custom-question-${customIndex}`;

        // 新たなlabel要素を作成（回答欄を表示するため）
        const answerLabel = document.createElement('label');
        answerLabel.textContent = `回答${customIndex + 1}:`;
        answerLabel.setAttribute('for', `custom-answer-${customIndex}`);

        // 新たなinput要素を作成（回答を入力するため）
        const answerInput = document.createElement('input');
        answerInput.type = 'text';
        answerInput.id = `custom-answer-${customIndex}`;
        answerInput.name = `custom-answer-${customIndex}`;

        // div要素に追加
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
         // カメラ起動中ならば，カメラを停止
         if (this.cameraHandler.cameraRunning){
            this.cameraHandler.stopCamera();
        }

        // 通常の質問時
        if (this.currentQuestionIndex < this.standardQuestions.length) {
            // 入力された値を取得し，保存
            if (this.standardQuestions[this.currentQuestionIndex] !== 'image') {
                const currentInput = document.getElementById(`answer-${this.currentQuestionIndex}`);
                this.standardQuestionsInput.push(currentInput.value);
            }

            // 現在の質問インデックスをインクリメント
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
        // 入力値確認（デバック用）
        console.log("通常の質問: ", this.standardQuestions)
        console.log("ユーザーが入力した値: ", this.standardQuestionsInput); // 全ての入力値を表示
        console.log("ユーザーが入力した追加質問: ", this.customQuestions); // 全ての追加質問を表示
        console.log("ユーザーが入力した追加質問の回答: ", this.customQuestionsInput); // 全ての追加質問の回答を表示

        this.nextButton.style.display = 'none'; // 次へボタンを隠す
        this.finishMessage.style.display = 'block'; // 終了メッセージを表示

        // Flaskにデータを送信
        this.sendQuestionnaire();
    }

    // Flaskに質問と回答をデータを送信するメソッド
    sendQuestionnaire() {
        // 通常質問の質問と回答をオブジェクトに変換
        const standardQuestionsData = this.standardQuestions.reduce((acc, question, index) => {
            acc[question] = this.standardQuestionsInput[index] || ''; // 回答がない場合も空文字を設定
            return acc;
        }, {});

        // 追加質問の質問と回答をオブジェクトに変換
        const customQuestionsData = this.customQuestions.reduce((acc, question, index) => {
            acc[question] = this.customQuestionsInput[index] || ''; // 回答がない場合も空文字を設定
            return acc;
        }, {});

        // 最終的な送信データを構成
        const dataToSend = {
            group_name: this.groupName,
            ...standardQuestionsData,
            ...customQuestionsData
        };

        // コンソールに表示（デバッグ用）
        console.log("送信するデータ: ", dataToSend);

        // Flaskにデータを送信
        fetch('/questions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dataToSend)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);

            //　リダイレクト
            window.location.href = '/complete';
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }

    // カメラキャプチャ画面を表示するメソッド
    showCameraCapture() {
        // 質問コンテナをクリア
        this.questionsContainer.innerHTML = '';

        this.cameraContainer.style.display = 'block';

        // カメラを起動
        this.cameraHandler.startCamera();

        // 撮影ボタンのクリックイベントリスナーを追加
        document.getElementById('capture-button').addEventListener('click', () => {
            const capturedDataUrl = this.cameraHandler.captureImage();
            this.standardQuestionsInput.push(capturedDataUrl);
    
            // 撮影した画像を表示する要素を取得
            const capturedImage = document.getElementById('captured-image');
            capturedImage.src = capturedDataUrl;
            capturedImage.style.display = 'block';
    
            // 撮影後に次へボタンを表示する
            const nextButton = document.getElementById('next-button');
            nextButton.style.display = 'block';
        });
    }

    selectCountry(index){
        // 新たなdiv要素を作成（グループ化するため）
        const questionDiv = document.createElement('div');
        questionDiv.className = 'question';

        // 新たなlabel要素を作成（質問文を表示するため）
        const questionLabel = document.createElement('label');
        questionLabel.textContent = "Country:";
        questionLabel.setAttribute('for', `answer-${index}`);

        // 新たなselect要素を作成（選択式の質問）
        const questionSelect = document.createElement('select');
        questionSelect.id = `answer-${index}`;
        questionSelect.name = `answer-${index}`;

        // 国の選択肢を追加
        const countries = ["Japan", "United States", "Canada", "Germany", "France", "Australia"];
        countries.forEach(country => {
            const option = document.createElement('option');
            option.value = country;
            option.textContent = country;
            questionSelect.appendChild(option);
        });

        // div要素に追加
        questionDiv.appendChild(questionLabel);
        questionDiv.appendChild(document.createElement('br'));
        questionDiv.appendChild(questionSelect);
        this.questionsContainer.appendChild(questionDiv);
    }

}

// 質問の配列を定義
const STANDARD_QUESTIONS = [
    "name",
    "age",
    "country",
    "favorite_things",
    "mbti",
    "image"
];

const CUSTOM_QUESTIONS_NUM = 1;

// Questionnaireクラスのインスタンスを作成
const questionnaire = new Questionnaire(STANDARD_QUESTIONS, CUSTOM_QUESTIONS_NUM, GROUP_NAME);

// 次へボタンのクリックイベントリスナーを追加
document.getElementById('next-button').addEventListener('click', () => {
    questionnaire.showNextQuestion();
});