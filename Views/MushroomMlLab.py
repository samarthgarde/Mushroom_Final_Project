import streamlit as st
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, auc, precision_recall_curve, precision_score, recall_score, f1_score, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    
    def set_bg_hack_url():

        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url("https://avi-chavan-96.sirv.com/Mushroom/fly-agaric-7515053_1280.jpg");
                background-size: 100% 100%;
                background-position: center;
                min-height: 100vh; /* Minimum height to cover the full viewport */
                height: auto; /* Adjust height based on content */
            }}
            </style>
            """,
            unsafe_allow_html=True)
    set_bg_hack_url()

    st.title("🍄The Mushroom ML Lab: LR,RF,SVM🌳")
    st.markdown("Are your mushrooms edible or poisonous? 🍄")
    st.sidebar.title("Mushroom Classifiers")
    st.sidebar.markdown("Upload a Mushroom Dataset and classify whether it's edible or poisonous!")

    @st.cache_data(persist=True)
    def preprocess_data(data):
        label = LabelEncoder()
        for col in data.columns:
            data[col] = label.fit_transform(data[col])
        return data

    @st.cache_data(persist=True)
    def split(df, target_column):
        y = df[target_column]
        x = df.drop(columns=[target_column])
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
        return x_train, x_test, y_train, y_test

    def plot_metrics(metrics_list, model, x_test, y_test, class_names):
        # Confusion Matrix
        if 'Confusion Matrix' in metrics_list:
            st.subheader("Confusion Matrix")
            cm = confusion_matrix(y_test, model.predict(x_test))
            fig, ax = plt.subplots()
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
            plt.ylabel('True label')
            plt.xlabel('Predicted label')
            st.pyplot(fig)

        # ROC Curve
        if 'ROC Curve' in metrics_list:
            st.subheader("ROC Curve")
            if hasattr(model, "predict_proba"):  # For models like Logistic Regression, RandomForest
                probs = model.predict_proba(x_test)[:, 1]
            else:  # For models like SVM that use decision_function
                probs = model.decision_function(x_test)
            fpr, tpr, _ = roc_curve(y_test, probs)
            roc_auc = auc(fpr, tpr)
            fig, ax = plt.subplots()
            ax.plot(fpr, tpr, color='blue', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
            ax.plot([0, 1], [0, 1], color='gray', linestyle='--')
            ax.set_xlim([0.0, 1.0])
            ax.set_ylim([0.0, 1.05])
            ax.set_xlabel('False Positive Rate')
            ax.set_ylabel('True Positive Rate')
            ax.set_title('Receiver Operating Characteristic (ROC) Curve')
            ax.legend(loc="lower right")
            st.pyplot(fig)

        # Precision-Recall Curve
        if 'Precision-Recall Curve' in metrics_list:
            st.subheader("Precision-Recall Curve")
            precision, recall, _ = precision_recall_curve(y_test, model.predict_proba(x_test)[:, 1])
            fig, ax = plt.subplots()
            ax.plot(recall, precision, color='blue', lw=2)
            ax.set_xlabel('Recall')
            ax.set_ylabel('Precision')
            ax.set_title('Precision-Recall Curve')
            st.pyplot(fig)

        # Recall vs Threshold Plot
        if 'Recall vs Threshold' in metrics_list:
            st.subheader("Recall vs Threshold")
            precision, recall, thresholds = precision_recall_curve(y_test, model.predict_proba(x_test)[:, 1])
            fig, ax = plt.subplots()
            ax.plot(thresholds, recall[:-1], color='green', lw=2)
            ax.set_xlabel('Threshold')
            ax.set_ylabel('Recall')
            ax.set_title('Recall vs Threshold')
            st.pyplot(fig)

        # F1-Score vs Threshold Plot
        if 'F1-Score vs Threshold' in metrics_list:
            st.subheader("F1-Score vs Threshold")
            precision, recall, thresholds = precision_recall_curve(y_test, model.predict_proba(x_test)[:, 1])
            f1_scores = 2 * (precision * recall) / (precision + recall)
            fig, ax = plt.subplots()
            ax.plot(thresholds, f1_scores[:-1], color='red', lw=2)
            ax.set_xlabel('Threshold')
            ax.set_ylabel('F1-Score')
            ax.set_title('F1-Score vs Threshold')
            st.pyplot(fig)

    # File uploader
    uploaded_file = st.sidebar.file_uploader("Upload a Mushroom Dataset CSV", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        possible_targets = ['type', 'class', 'class=e', 'class=p']
        target_column = None
        for col in possible_targets:
            if col in data.columns:
                target_column = col
                break

        if target_column is None:
            # Automatically choose the last column as the target if no expected column is found
            target_column = data.columns[-1]
            st.warning(f"Using '{target_column}' as the target column since no expected column was found.")

        
        df = preprocess_data(data)
        x_train, x_test, y_train, y_test = split(df, target_column)
        class_names = ['edible', 'poisonous']

        # Toggle dataset visibility
        if st.sidebar.checkbox("Show Dataset", False):
            st.subheader("Mushroom Dataset (Processed for Classification)")
            st.write(data)

        st.sidebar.subheader("Choose Classifier:")
        classifier = st.sidebar.selectbox(
            "Classifier",
            ("Logistic Regression", "Random Forest","Support Vector Machines (SVM)")
        )
        
        if classifier == 'Support Vector Machines (SVM)':
            st.sidebar.subheader("Model Hyperparameters")
            C = st.sidebar.number_input("C (Regularization Parameter)", 0.1, 10.0, step=0.1, key='C')
            kernel = st.sidebar.radio("Kernel", ("rbf", "linear"), key='kernel')
            gamma = st.sidebar.radio("Gamma (Kernel Coefficient)", ("scale", "auto"), key='gamma')
            metrics = st.sidebar.multiselect("What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve', 'Recall vs Threshold', 'F1-Score vs Threshold'))

            if st.sidebar.button("Classify", key='classify'):
                st.subheader("Support Vector Machine (SVM) Results")
                model = SVC(C=C, kernel=kernel, gamma=gamma, probability=True)
                model.fit(x_train, y_train)
                y_pred = model.predict(x_test)
                accuracy = accuracy_score(y_test, y_pred)
                st.write("Accuracy: ", round(accuracy, 2))
                st.write("Precision: ", round(precision_score(y_test, y_pred), 2))
                st.write("Recall: ", round(recall_score(y_test, y_pred), 2))
                st.write("F1-Score: ", round(f1_score(y_test, y_pred), 2))

                # Define X for predictions
                X = df.drop(columns=[target_column])  # Drop target_column for predictions
                all_predictions = model.predict(X)
                predicted_labels = ["Edible" if pred == 0 else "Poisonous" for pred in all_predictions]
                results_df = data.copy()
                results_df['Prediction'] = predicted_labels

                # Display results
                st.subheader("Classification Results")
                st.dataframe(results_df)

                # Count edible and poisonous mushrooms
                edible_count = predicted_labels.count("Edible")
                poisonous_count = predicted_labels.count("Poisonous")
                st.write(f"Number of edible mushrooms: {edible_count}")
                st.write(f"Number of poisonous mushrooms: {poisonous_count}")

                # Plot metrics
                plot_metrics(metrics, model, x_test, y_test, class_names)

            

        if classifier == 'Logistic Regression':
            st.sidebar.subheader("Model Hyperparameters")
            C = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key='C_LR')
            max_iter = st.sidebar.slider("Maximum number of iterations", 100, 500, key='max_iter')
            metrics = st.sidebar.multiselect("What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve', 'Recall vs Threshold', 'F1-Score vs Threshold'))

            if st.sidebar.button("Classify", key='classify'):
                st.subheader("Logistic Regression Results")
                model = LogisticRegression(C=C, max_iter=max_iter, solver='liblinear')
                model.fit(x_train, y_train)
                y_pred = model.predict(x_test)
                accuracy = accuracy_score(y_test, y_pred)
                st.write("Accuracy: ", round(accuracy, 2))
                st.write("Precision: ", round(precision_score(y_test, y_pred), 2))
                st.write("Recall: ", round(recall_score(y_test, y_pred), 2))
                st.write("F1-Score: ", round(f1_score(y_test, y_pred), 2))

                # Define X for predictions
                X = df.drop(columns=[target_column])  # Drop target_column for predictions
                all_predictions = model.predict(X)
                predicted_labels = ["Edible" if pred == 0 else "Poisonous" for pred in all_predictions]
                results_df = data.copy()
                results_df['Prediction'] = predicted_labels

                # Display results
                st.subheader("Classification Results")
                st.dataframe(results_df)

                # Count edible and poisonous mushrooms
                edible_count = predicted_labels.count("Edible")
                poisonous_count = predicted_labels.count("Poisonous")
                st.write(f"Number of edible mushrooms: {edible_count}")
                st.write(f"Number of poisonous mushrooms: {poisonous_count}")

                # Plot metrics
                plot_metrics(metrics, model, x_test, y_test, class_names)

        if classifier == 'Random Forest':
            st.sidebar.subheader("Model Hyperparameters")
            n_estimators = st.sidebar.number_input("Number of trees in the forest", 100, 5000, step=10, key='n_estimators')
            max_depth = st.sidebar.number_input("Maximum depth of the tree", 1, 20, step=1, key='max_depth')
            bootstrap = st.sidebar.radio("Bootstrap samples when building trees", ('True', 'False'), key='bootstrap') == 'True'
            metrics = st.sidebar.multiselect("What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve', 'Recall vs Threshold', 'F1-Score vs Threshold'))

            if st.sidebar.button("Classify", key='classify'):
                st.subheader("Random Forest Results")
                model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, bootstrap=bootstrap, n_jobs=-1)
                model.fit(x_train, y_train)
                y_pred = model.predict(x_test)
                accuracy = accuracy_score(y_test, y_pred)
                st.write("Accuracy: ", round(accuracy, 2))
                st.write("Precision: ", round(precision_score(y_test, y_pred), 2))
                st.write("Recall: ", round(recall_score(y_test, y_pred), 2))
                st.write("F1-Score: ", round(f1_score(y_test, y_pred), 2))
                
                # Define X for predictions
                X = df.drop(columns=[target_column])  # Drop target_column for predictions
                all_predictions = model.predict(X)
                predicted_labels = ["Edible" if pred == 0 else "Poisonous" for pred in all_predictions]
                results_df = data.copy()
                results_df['Prediction'] = predicted_labels

                # Display results
                st.subheader("Classification Results")
                st.dataframe(results_df)

                # Count edible and poisonous mushrooms
                edible_count = predicted_labels.count("Edible")
                poisonous_count = predicted_labels.count("Poisonous")
                st.write(f"Number of edible mushrooms: {edible_count}")
                st.write(f"Number of poisonous mushrooms: {poisonous_count}")

                # Plot metrics
                plot_metrics(metrics, model, x_test, y_test, class_names)

        if classifier == 'Decision Tree':
            st.sidebar.subheader("Model Hyperparameters")
            max_depth = st.sidebar.number_input("Maximum depth of the tree", 1, 20, step=1, key='max_depth_dt')
            metrics = st.sidebar.multiselect("What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve', 'Recall vs Threshold', 'F1-Score vs Threshold'))

            if st.sidebar.button("Classify", key='classify'):
                st.subheader("Decision Tree Results")
                model = DecisionTreeClassifier(max_depth=max_depth)
                model.fit(x_train, y_train)
                y_pred = model.predict(x_test)
                accuracy = accuracy_score(y_test, y_pred)
                st.write("Accuracy: ", round(accuracy, 2))
                st.write("Precision: ", round(precision_score(y_test, y_pred), 2))
                st.write("Recall: ", round(recall_score(y_test, y_pred), 2))
                st.write("F1-Score: ", round(f1_score(y_test, y_pred), 2))

                # Display the count of edible and poisonous mushrooms
                edible_count = np.sum(y_pred == 0)  # Assuming 0 is "edible"
                poisonous_count = np.sum(y_pred == 1)  # Assuming 1 is "poisonous"
                st.write(f"Number of edible mushrooms: {edible_count}")
                st.write(f"Number of poisonous mushrooms: {poisonous_count}")
                
                plot_metrics(metrics, model, x_test, y_test, class_names)

        if classifier == 'K-Nearest Neighbors (KNN)':
            st.sidebar.subheader("Model Hyperparameters")
            n_neighbors = st.sidebar.number_input("Number of neighbors", 1, 20, step=1, key='n_neighbors')
            metrics = st.sidebar.multiselect("What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve', 'Recall vs Threshold', 'F1-Score vs Threshold'))

            if st.sidebar.button("Classify", key='classify'):
                st.subheader("K-Nearest Neighbors (KNN) Results")
                model = KNeighborsClassifier(n_neighbors=n_neighbors)
                model.fit(x_train, y_train)
                y_pred = model.predict(x_test)
                accuracy = accuracy_score(y_test, y_pred)
                st.write("Accuracy: ", round(accuracy, 2))
                st.write("Precision: ", round(precision_score(y_test, y_pred), 2))
                st.write("Recall: ", round(recall_score(y_test, y_pred), 2))
                st.write("F1-Score: ", round(f1_score(y_test, y_pred), 2))

                # Display the count of edible and poisonous mushrooms
                edible_count = np.sum(y_pred == 0)  # Assuming 0 is "edible"
                poisonous_count = np.sum(y_pred == 1)  # Assuming 1 is "poisonous"
                st.write(f"Number of edible mushrooms: {edible_count}")
                st.write(f"Number of poisonous mushrooms: {poisonous_count}")
                
                plot_metrics(metrics, model, x_test, y_test, class_names)

        if classifier == 'Naive Bayes':
            st.sidebar.subheader("Model Hyperparameters")
            metrics = st.sidebar.multiselect("What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve', 'Recall vs Threshold', 'F1-Score vs Threshold'))

            if st.sidebar.button("Classify", key='classify'):
                st.subheader("Naive Bayes Results")
                model = GaussianNB()
                model.fit(x_train, y_train)
                y_pred = model.predict(x_test)
                accuracy = accuracy_score(y_test, y_pred)
                st.write("Accuracy: ", round(accuracy, 2))
                st.write("Precision: ", round(precision_score(y_test, y_pred), 2))
                st.write("Recall: ", round(recall_score(y_test, y_pred), 2))
                st.write("F1-Score: ", round(f1_score(y_test, y_pred), 2))

                # Display the count of edible and poisonous mushrooms
                edible_count = np.sum(y_pred == 0)  # Assuming 0 is "edible"
                poisonous_count = np.sum(y_pred == 1)  # Assuming 1 is "poisonous"
                st.write(f"Number of edible mushrooms: {edible_count}")
                st.write(f"Number of poisonous mushrooms: {poisonous_count}")
                
                plot_metrics(metrics, model, x_test, y_test, class_names)
    # Footer with social links
    st.markdown('<div class="footer">Created with ❤️ by Strategic Synergists</div>', unsafe_allow_html=True)

