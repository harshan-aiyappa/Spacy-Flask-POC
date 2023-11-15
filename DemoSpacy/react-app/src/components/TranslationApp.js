// TranslationApp.jsx

import React, { useState } from 'react';
import axios from 'axios';
import './TranslationApp.css';

const TranslationApp = () => {
  const [textToTranslate, setTextToTranslate] = useState('');
  const [targetLanguage, setTargetLanguage] = useState('en');
  const [translationResult, setTranslationResult] = useState('');

  const handleTranslate = async (translator) => {
    try {
      const response = await axios.post(`http://localhost:5000/translate/${translator}`, {
        text: textToTranslate,
        target_language: targetLanguage,
      });

      setTranslationResult(response.data.translated_text);
    } catch (error) {
      console.error('Error translating text:', error.message);
    }
  };


  const handleTranslateWithTranslator = async () => {
    try {
      const response = await axios.post('http://localhost:5000/translate/translator', {
        text: textToTranslate,
        from_lang: 'en', // You can change the source language as needed
        to_lang: targetLanguage,
      });

      setTranslationResult(response.data.translated_text);
    } catch (error) {
      console.error('Error translating text with Translator:', error.message);
    }
  };
  
  const languageOptions = [
    { label: 'English', value: 'en' },
    { label: 'Portuguese', value: 'pt' },
    { label: 'Spanish', value: 'es' },
    { label: 'French', value: 'fr' },
    { label: 'German', value: 'de' },
  ];

  return (
    <div className="container">
      <label className="label">
        <h3>Enter text to translate: </h3> 
        <input
          type="text"
          value={textToTranslate}
          onChange={(e) => setTextToTranslate(e.target.value)}
          className="input"
        />
      </label>

      <div className="radioContainer">
        <h3>Choose target language: </h3>
        {languageOptions.map((language) => (
          <label key={language.value} className="radioLabel">
            <input
              type="radio"
              value={language.value}
              checked={targetLanguage === language.value}
              onChange={() => setTargetLanguage(language.value)}
            />
            {language.label}
          </label>
        ))}
      </div>

      <div>
        <button onClick={() => handleTranslate('mymemory')} className="button">
          Translate (MyMemory)
        </button>
        <button onClick={() => handleTranslate('google')} className="button">
          Translate (Google)
        </button>
        <button onClick={() => handleTranslate('pons')} className="button">
          Translate (Pons)
        </button>
        <button onClick={() => handleTranslate('linguee')} className="button">
          Translate (Linguee)
        </button>
        {/* <button onClick={handleTranslateWithTranslator} className="button">
          Translate (Translator)
        </button> */}
      </div>

      <div className="result">
        <p>Translation Result:</p>
        <p>{translationResult}</p>
      </div>
    </div>
  );
};

export default TranslationApp;
