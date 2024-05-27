import streamlit as st

def calculate_reward_risk(entry, profit_target, stop_loss):
    potential_gain = profit_target - entry
    potential_loss = entry - stop_loss
    reward_risk_ratio = potential_gain / abs(potential_loss)
    required_win_rate = 1 / (1 + reward_risk_ratio) * 100
    return reward_risk_ratio, potential_gain, potential_loss, required_win_rate


st.title("Reward/Risk Ratio Calculator")

entry_price = st.number_input("Entry price", value=237.65, step=0.01)
profit_target = st.number_input("Profit target", value=275.00, step=0.01)
stop_loss = st.number_input("Stop loss", value=210.00, step=0.01)

if st.button("Calculate"):
    reward_risk_ratio, potential_gain, potential_loss, required_win_rate = calculate_reward_risk(entry_price,
                                                                                                 profit_target,
                                                                                                 stop_loss)

    st.write(f"**Reward/risk ratio**: {reward_risk_ratio:.2f}")
    st.write(f"**Potential gain**: ${potential_gain:.2f}")
    st.write(f"**Potential loss**: ${potential_loss:.2f}")
    st.write(f"**Required win-rate for consistent profitability**: {required_win_rate:.2f}%")