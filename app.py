import streamlit as st


# Function to calculate reward/risk ratio and required win rate
def calculate_reward_risk(entry_price, profit_target, stop_loss):
    potential_gain = profit_target - entry_price
    potential_loss = entry_price - stop_loss
    reward_risk_ratio = potential_gain / abs(potential_loss)
    required_win_rate = 1 / (1 + reward_risk_ratio) * 100
    return reward_risk_ratio, potential_gain, potential_loss, required_win_rate


st.title("Reward/Risk Ratio Calculator")

# Input fields
entry_price = st.number_input("Enter the entry price", value=237.65, step=0.01)
profit_target = st.number_input("Enter the profit target", value=275.00, step=0.01)
stop_loss = st.number_input("Enter the stop loss", value=210.00, step=0.01)

if st.button("Calculate"):
    reward_risk_ratio, potential_gain, potential_loss, required_win_rate = calculate_reward_risk(entry_price,
                                                                                                 profit_target,
                                                                                                 stop_loss)

    st.write(f"**Reward/Risk Ratio**: {reward_risk_ratio:.2f}")
    st.write(f"**Potential Gain**: ${potential_gain:.2f}")
    st.write(f"**Potential Loss**: ${potential_loss:.2f}")
    st.write(f"**Required Win Rate for Consistent Profitability**: {required_win_rate:.2f}%")

st.write("Follow me on X [@foundervisions](https://x.com/foundervisions)")

