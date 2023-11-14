import React, { useState } from "react";
import axios from "axios";
import languageData from "./languageData";
import TokenInfo from "./components/TokenInfo";
console.log(languageData);
const NlpComponent = () => {
  const [text, setText] = useState("");
  const [tokens, setTokens] = useState([]);
  const [entities, setEntities] = useState([]);
  const [posTags, setPosTags] = useState([]);
  const [dependencies, setDependencies] = useState([]);
  const [lemmas, setLemmas] = useState([]);
  const [allTokensData, setAllTokensData] = useState([]);
  const [selectedLanguage, setSelectedLanguage] = useState("en"); // Default selected language

  const handleLanguageChange = (event) => {
    setSelectedLanguage(event.target.value);
  };

  const handleTokenize = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/tokenize", {
        text,
        lng: selectedLanguage,
      });
      console.log("tokenizing :", response.data);
      setTokens(response.data);
    } catch (error) {
      console.error("Error tokenizing text:", error);
    }
  };

  const handleNER = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/ner", {
        text,
        lng: selectedLanguage,
      });
      console.log("NER :", response.data);
      setEntities(response.data);
    } catch (error) {
      console.error("Error performing NER:", error);
    }
  };

  const handlePosTagging = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/pos", {
        text,
        lng: selectedLanguage,
      });
      console.log("POS tagging :", response.data);
      setPosTags(response.data);
    } catch (error) {
      console.error("Error performing POS tagging:", error);
    }
  };

  const handleDependencyParsing = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/dependency", {
        text,
        lng: selectedLanguage,
      });
      console.log("dependency :", response.data);
      setDependencies(response.data);
    } catch (error) {
      console.error("Error performing dependency parsing:", error);
    }
  };

  const handleLemmatization = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/lemmatize", {
        text,
        lng: selectedLanguage,
      });
      console.log("lemmatization :", response.data);
      setLemmas(response.data);
    } catch (error) {
      console.error("Error performing lemmatization:", error);
    }
  };
  const handleTokensAttributtes = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/analyze", {
        text,
        lng: selectedLanguage,
      });
      console.log("Tokens Attributte :", response.data);
      setAllTokensData(response.data);
    } catch (error) {
      console.error("Error performing lemmatization:", error);
    }
  };

  let languageObj = {
    en: "English",
    pt: "Portuguese",
    es: "Spanish",
  };

  const [selectedTargetLanguage, setSelectedTargetLanguage] = useState("");
  const [translatedText, setTranslatedText] = useState("");

  const handleTargetLanguageClick = (languageCode) => {
    console.log("Target language", languageCode);
    setSelectedTargetLanguage(languageCode);
  };

  const handleTranslation = async () => {
    try {
      const response = await axios.post("http://localhost:5000/translate", {
        text: text,
        from_lang: selectedLanguage,
        to_lang: selectedTargetLanguage,
      });

      console.log("Translated Text:", response.data.translated_text);
      setTranslatedText(response.data.translated_text);
    } catch (error) {
      console.error("Error performing translation:", error);
    }
  };

  const [synonymsAntonyms, setSynonymsAntonyms] = useState({});
  const [tokenInfoData, setTokeInfoData] = useState([]);
  const handleGetTokenInfo = async () => {
    try {
      const response = await axios.post(
        "http://localhost:5000/get_token_info",
        {
          sentence: text,
          lang: selectedLanguage,
        }
      );
  
      console.log("Token Info:", response.data);
      setTokeInfoData(response.data);
    } catch (error) {
      console.error("Error getting token information:", error);
    }
  };

  const handleSynonymsAntonyms = async () => {
    try {
      const response = await axios.post(
        "http://localhost:5000/synonyms_antonyms",
        {
          word: text,
          lang: selectedLanguage,
        }
      );

      console.log("Synonyms & Antonyms are :", response.data);
      setSynonymsAntonyms(response.data);
    } catch (error) {
      console.error("Error performing translation:", error);
    }
  };

  React.useEffect(() => {
    if (selectedTargetLanguage) {
      handleTranslation();
    }
  }, [selectedTargetLanguage]);

  return (
    <div className="nlp-container">
      <h2 style={{ textAlign: "center" }}> spaCy and Flask</h2>
      <div className="json-pre">
        <h2>Select a Language:</h2>
        <div className="language-selection">
          <label>
            <input
              type="radio"
              value="en"
              checked={selectedLanguage === "en"}
              onChange={handleLanguageChange}
            />
            English
          </label>

          <label>
            <input
              type="radio"
              value="pt"
              checked={selectedLanguage === "pt"}
              onChange={handleLanguageChange}
            />
            Portuguese
          </label>

          <label>
            <input
              type="radio"
              value="es"
              checked={selectedLanguage === "es"}
              onChange={handleLanguageChange}
            />
            Spanish
          </label>
        </div>
        <p>
          Selected Language: <b>{languageObj[selectedLanguage]}</b>
        </p>
      </div>
      <textarea
        className="input-text"
        rows="2"
        cols="80"
        placeholder="Enter text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <div className="results-container">
        {" "}
        <button className={"css-button-3d--blue"} onClick={handleTokenize}>
          Tokenize
        </button>
        <button className={"css-button-3d--blue"} onClick={handleNER}>
          Named Entity Recognition (NER)
        </button>
        <button className={"css-button-3d--blue"} onClick={handlePosTagging}>
          Part-of-Speech (POS) Tagging
        </button>
        <button
          className={"css-button-3d--blue"}
          onClick={handleDependencyParsing}
        >
          Dependency Parsing
        </button>
        <button className={"css-button-3d--blue"} onClick={handleLemmatization}>
          Lemmatization
        </button>
        <button
          className={"css-button-3d--blue"}
          onClick={handleTokensAttributtes}
        >
          Tokens JSON
        </button>
        <button
          className={"css-button-3d--blue"}
          onClick={handleGetTokenInfo}
        >
          Tokens Info
        </button>
        <button
          className={"css-button-3d--blue"}
          onClick={handleSynonymsAntonyms}
        >
          Synonyms & Antonyms
        </button>
        <div>
          <h2>Convert to Language:</h2>
          {languageData.map((language) => (
            <button
              style={{
                height: "40px",
                fontSize: "1em",
                color: "#fff",
                padding: "5px 10px",
                fontWeight: "bold",
                cursor: "pointer",
                transition: "all 0.3s ease",
                position: "relative",
                display: "inline-block",
                outline: "none",
                borderRadius: "5px",
                zIndex: "0",
                background: language.color,
                overflow: "hidden",
                border: `2px solid ${language.color}`,
                margin: ".5em",
              }}
              // Hover effect styles
              onMouseEnter={(e) => {
                e.target.style.backgroundColor = "#fff"; // Hover background color
                e.target.style.color = "#164863"; // Hover text color
              }}
              onMouseLeave={(e) => {
                e.target.style.backgroundColor = language.color; // Restore original background color
                e.target.style.color = "#fff"; // Restore original text color
              }}
              key={`target-${language.code}`}
              type="button"
              onClick={() => handleTargetLanguageClick(language.code)}
            >
              {language.name}
            </button>
          ))}
        </div>
      </div>

      <div>
        <h3>Translation Text ( {selectedTargetLanguage} ):</h3>
        <ul className="json-pre">
          {translatedText && (
            <div>
              <p>{translatedText}</p>
            </div>
          )}
        </ul>
      </div>
      <div>
        <h2>{`Word: ${text}`}</h2>
        <div>
          <h3>Synonyms:</h3>
          {synonymsAntonyms.synonyms ? (
            <ul>
              {synonymsAntonyms.synonyms.map((synonym, index) => (
                <li style={{ listStyleType: "square" }} key={index}>
                  {synonym}
                </li>
              ))}
            </ul>
          ) : (
            <p>No synonyms available</p>
          )}
        </div>
        <div>
          <h3>Antonyms:</h3>
          {synonymsAntonyms.antonyms ? (
            <ul className="json-pre">
              {synonymsAntonyms.antonyms.map((antonym, index) => (
                <li key={index}>{antonym}</li>
              ))}
            </ul>
          ) : (
            <p>No antonyms available</p>
          )}
        </div>
      </div>
      <div>
        <h3>Tokens</h3>
        <ul className="json-pre">
          {tokens.map((token, index) => (
            <li key={index}>[ {token} ]</li>
          ))}
        </ul>
      </div>
      <div>
        <h3>Named Entities</h3>
        <ul className="json-pre">
          {entities.map((entity, index) => (
            <li key={index}>[ {`${entity.text} => ${entity.label}`} ]</li>
          ))}
        </ul>
      </div>
      <div>
        <h3>POS Tags</h3>
        <ul className="json-pre">
          {posTags.map((tag, index) => (
            <li key={index}>
              [{" "}
              {`${tag.text} => (in high level) : (${tag.pos} - ${tag.posExplain}) -> (in depth) :  (${tag.tagger} - ${tag.taggerExplain}) `}{" "}
              ]
            </li>
          ))}
        </ul>
      </div>
      <div>
        <h3>Dependencies</h3>
        <ul className="json-pre">
          {dependencies.map((dep, index) => (
            <li key={index}>[ {`${dep.text} => ${dep.dep}`} ]</li>
          ))}
        </ul>
      </div>
      <div>
        <h3>Lemmas</h3>
        <ul className="json-pre">
          {lemmas.map((lemma, index) => (
            <li key={index}>[ {`${lemma.text} => ${lemma.lemma}`} ]</li>
          ))}
        </ul>
      </div>
      <div>
        <h1>Token Attributes</h1>
        {allTokensData ? (
          <pre className="json-pre">
            {JSON.stringify(allTokensData, null, 2)}
          </pre>
        ) : (
          <p>Loading data...</p>
        )}
      </div>
      <div>
        <h1>Token info</h1>
        {tokenInfoData ? (
         <TokenInfo tokenData={tokenInfoData} />
        ) : (
          <p>Loading data...</p>
        )}
      </div>
    </div>
  );
};

export default NlpComponent;
