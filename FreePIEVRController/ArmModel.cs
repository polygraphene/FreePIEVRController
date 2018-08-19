using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FreePIEVRController
{
    public class ArmModel
    {
        // from eyes to elbow in meters
        private static readonly double[] EYES_TO_ELBOW = { 0.175, -0.3, -0.03 };
        // from elbow to forearm in meters
        private static readonly double[] FOREARM = { 0.0, 0.0, -0.175 };

        private static readonly double USER_HEIGHT = 1.7;

        public static double[] CalculateModel(double[] quaternion)
        {
            double[] position = new double[3];
            position[0] = EYES_TO_ELBOW[0] * USER_HEIGHT;
            position[1] = EYES_TO_ELBOW[1] * USER_HEIGHT;
            position[2] = EYES_TO_ELBOW[2] * USER_HEIGHT;

            var vec = QuaternionVectorRotate(quaternion, FOREARM);

            position[0] += vec[0];
            position[1] += vec[1];
            position[2] += vec[2];
            return position;
        }

        private static double[] QuaternionMultiply(double[] a, double[] b)
        {
            double[] ret = new double[4];
            ret[0] = a[0] * b[3] + a[1] * b[2] - a[2] * b[1] + a[3] * b[0];
            ret[1] = -a[0] * b[2] + a[1] * b[3] + a[2] * b[0] + a[3] * b[1];
            ret[2] = a[0] * b[1] - a[1] * b[0] + a[2] * b[3] + a[3] * b[2];
            ret[3] = -a[0] * b[0] - a[1] * b[1] - a[2] * b[2] + a[3] * b[3];
            return ret;
        }

        private static double[] QuaternionVectorRotate(double[] q, double[] v)
        {
            double[] q2 = new double[4];
            q2[0] = -q[0];
            q2[1] = -q[1];
            q2[2] = -q[2];
            q2[3] = q[3];
            double[] qv = new double[4];
            qv[0] = v[0];
            qv[1] = v[1];
            qv[2] = v[2];
            qv[3] = 0;
            return QuaternionMultiply(QuaternionMultiply(q, qv), q2);
        }
    }
}
