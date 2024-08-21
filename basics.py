{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "609c3873-9f1f-41f4-a6e3-9f1523678d6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4160440c-fadc-46c4-ab59-6ea42bb251da",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_angle(a, b, c):\n",
    "    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])\n",
    "    angle = np.abs(np.degrees(radians))\n",
    "    \n",
    "    return angle\n",
    "\n",
    "def get_distance(landmarks_list):\n",
    "    if len(landmarks_list) < 2:\n",
    "        return\n",
    "\n",
    "    (x1, y1), (x2, y2) = landmark_list[0], landmark_list[1]\n",
    "    L = np.hypot(x2 - x1, y2 - y1)\n",
    "    return np.interp(L, [0, 1], (0, 1000))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
