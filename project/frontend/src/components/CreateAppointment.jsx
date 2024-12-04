import React, { useState } from "react";
import axios from "axios";

const CreateAppointment = () => {
  const [formData, setFormData] = useState({
    patient_name: "",
    email: "",
    date: "",
    time: "",
    reason: "",
  });
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  const createAppointment = async () => {
    try {
      const res = await axios.post("/appointments", formData);
      setResponse(res.data);
      setError(null);
    } catch (err) {
      setError(err.response?.data?.error || "An error occurred");
    }
  };

  return (
    <div>
      <h3>Create Appointment</h3>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          createAppointment();
        }}
      >
        <input
          type="text"
          placeholder="Patient Name"
          value={formData.patient_name}
          onChange={(e) => setFormData({ ...formData, patient_name: e.target.value })}
          required
        />
        <input
          type="email"
          placeholder="Email"
          value={formData.email}
          onChange={(e) => setFormData({ ...formData, email: e.target.value })}
          required
        />
        <input
          type="date"
          value={formData.date}
          onChange={(e) => setFormData({ ...formData, date: e.target.value })}
          required
        />
        <input
          type="time"
          value={formData.time}
          onChange={(e) => setFormData({ ...formData, time: e.target.value })}
          required
        />
        <textarea
          placeholder="Reason"
          value={formData.reason}
          onChange={(e) => setFormData({ ...formData, reason: e.target.value })}
          required
        ></textarea>
        <button type="submit">Create Appointment</button>
      </form>
      {response && <p>{response.message}</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
};

export default CreateAppointment;

