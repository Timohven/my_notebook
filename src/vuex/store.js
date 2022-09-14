import { createStore } from 'vuex'
import axios from 'axios'

const store = createStore({
  state: {
    notes: [],
    active_note: null 
  },
  mutations: {
    SET_NOTES_TO_STATE: (state, notes) => {
      state.notes = notes;
    },
    SET_ACTIVE_NOTE: (state, ind) => {
      if (ind == -1) {
        state.active_note = { 'note_id' : ind,
                              'title' : 'new title',
                              'category' : 1,
                              'content' : 'new note',
                              'creation_data' : null,
                              'last_edit__data' : null
                            };
      } else {
        state.active_note = state.notes[ind];
      }
    },
    SAVE_ACTIVE_NOTE: (state) => { 
      console.log("NEW ADD!!!");
      if (state.active_note.note_id==-1) {
        console.log('content new note:', state.active_note);
        axios.post('http://127.0.0.1:5000/add', {data: state.active_note})
          .then(response => console.log("NEW ADD:", state.active_note, 'RESPONSE:', response))
          .catch(response => console.log("NEW ADD ERROR:", response)); 
        } else {
          console.log('content active note:', state.active_note);
          axios.post('http://127.0.0.1:5000/update', {data: state.active_note})
            .then(response => console.log("UPDATE", state.active_note, 'RESPONSE:', response))
            .catch(response => console.log("UPDATE ERROR:", response));         
        } 
      state.active_note = [];
    },
    CANCEL_STATE: (state) => { 
      state.active_note = []; 
    }
  },
  actions: {
    GET_NOTES_FROM_API({commit}) {
        // const response = await get('http://localhost:3000/notes');
        // commit('SET_NOTES_TO_STATE', response.notes.data);
      
      console.log("request axios notes");
      return axios('http://127.0.0.1:5000/notes', {
      // return axios('http://localhost:3000/data', {
        method: "GET"
      })
        .then((notes) => {
          commit('SET_NOTES_TO_STATE', notes.data.data);
          // commit('SET_NOTES_TO_STATE', notes.data);
          console.log(notes.data);
          return notes;
        })
        .catch((error) => {
          console.log("ERROR!");
          return error;
        })
    },
    EDIT_NOTE ({commit}, ind) {
      commit('SET_ACTIVE_NOTE', ind);
    },
    SAVE_NOTE ({commit}) {
      commit('SAVE_ACTIVE_NOTE')
    },
    CANCEL ({commit}) {
      commit('CANCEL_STATE')
    }
  },
  getters: {
    NOTES(state) {
      return state.notes;
    },
    ACTIVE_NOTE(state) {
      return state.active_note;
    }
  }
})


export default store;