import { useState } from "react";
import axios from 'axios';

function App() {

  const [message, setMessage] = useState('Dear future me, ');
  const [date, setDate] = useState('');
  const [email, setEmail] = useState('');

  const [view, setView] = useState('lp');

  const save_msg = async () => {
    let req_url = process.env.REQUEST_URL || 'http://localhost:8000'
    const res = await axios.post(req_url + '/api/save_msg', {
      recipient_email:email,
      message_body: message,
      scheduled_date:date
    })

    const data = await res.data

    if (data.status == 200) {
      setView('sent');
    } else {
      alert('Error')
    }

  }

  if (view == 'lp') {

    return (
      <main className="w-full h-[100vh] bg-orange-200/30 flex flex-col items-center justify-center">
        <header className="fixed top-4 left-4">
            <h1 className="text-3xl font-black text-slate-700 leading-none">Tomorrow</h1>
            <h4 className="text-3xl font-black text-slate-700 leading-none -mt-1">You</h4>
        </header>
        <section>
          <form className="flex flex-col items-start w-[95vw] md:w-[60vw]">
            <h3 className="text-3xl text-slate-800">Leave a message to your future-self.</h3>
            <p className="font-black text-xl">Start writing!</p>
            <main className="flex flex-row w-full">
              <textarea className="w-full min-h-60 mt-1 shadow-xl rounded-lg p-2" value={message} onChange={(e) => setMessage(e.target.value)}></textarea>
            <aside className="max-w-72 ml-4 flex flex-col gap-4">
              <span>
                  <label className="font-black">Deliver In</label>
                  <input value={date} onChange={(e) => setDate(e.target.value)}  type="date" className="w-full mt-1 p-2 rounded-md shadow-md"></input>             
              </span>
              <span>
                  <label className="font-black">In which email?</label>
                  <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" placeholder="foo@bar.com" className="w-full mt-1 p-2 rounded-md shadow-md"></input>             
              </span>
  
              <button onClick={save_msg} type="button" class="btn-custom">
                <strong>Travel time</strong>
                <div id="container-stars">
                  <div id="stars"></div>
                </div>
  
                <div id="glow">
                  <div class="circle"></div>
                  <div class="circle"></div>
                </div>
            </button>
  
            </aside>
            </main>
          </form>
        </section>
      </main>
    );
  } else {
    return (
      <main className="w-full h-[100vh] bg-orange-200/30 flex flex-col items-center justify-center">
        <header className="fixed top-4 left-4">
            <h1 className="text-3xl font-black text-slate-700 leading-none">Tomorrow</h1>
            <h4 className="text-3xl font-black text-slate-700 leading-none -mt-1">You</h4>
        </header>
        <section className="bg-white flex flex-col items-center p-4 shadow-2xl rounded-lg md:p-8">
          <h1 className="font-black text-slate-700 text-3xl">Congratulations, Time Traveler!</h1>
          <img src="/check.png" className="w-48"></img>
          <p className="w-[350px] text-center font-black">
            One day, in the future, you'll receive these very words, a gift from your past.
          </p>
        </section>
      </main>
    );
  }
}

export default App;
