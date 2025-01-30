def unitify(magnitude):
	m_units = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
	while magnitude > 1024 and len(m_units)-1:
		magnitude /= 1024
		m_units.pop(0)
	return f"{round(magnitude, 2)} {m_units[0]}"
	